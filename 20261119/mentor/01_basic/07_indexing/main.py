"""실습 07 Basic · 기본 실행은 데이터 계약, --live-db는 실제 E5/DB 실행."""  # 이 파일의 실행 모드와 목표를 설명합니다.
from pathlib import Path  # 현재 파일의 위치를 안전하게 다루기 위해 Path를 가져옵니다.
import sys  # 명령줄 인자를 확인하고 Python 모듈 검색 경로를 조정하기 위해 가져옵니다.
HERE=Path(__file__).resolve().parent  # 현재 main.py가 위치한 폴더의 절대 경로를 저장합니다.
sys.path.insert(0,str(HERE.parents[1]))  # mentor 루트를 모듈 검색 경로 앞에 넣어 coursekit을 찾게 합니다.
from coursekit.io import save_json, show_success  # 결과 JSON 저장과 완료 메시지 출력을 가져옵니다.
from coursekit.documents import by_doc,parse_one  # 문서 검색과 문서 파싱 함수를 가져옵니다.
from coursekit.processing import make_chunks  # 파싱된 문서에서 청크를 만드는 함수를 가져옵니다.


def select_index_chunk(doc_id:str)->tuple[dict,dict]:  # 문서 ID를 받아 인덱싱할 문서와 청크를 돌려줍니다.
    # BEGIN D24-07-B01
    # 개념·실무 해설: Indexing 입력은 검증된 Chunk의 내용과 출처입니다. 임의로 만든 384개 숫자를 E5 Embedding이라 부르지 않습니다.
    # 해설 D24-07-B01 : 기존 DOC-ASSIGN 텍스트에서 유효한 청크 1건을 선택하고 E5 passage 입력을 확인합니다.
    # 입력·출력은 함수 시그니처와 docstring에 따릅니다.
    # 이 블록은 예제를 따라 실행하며 검증 가능한 결과를 반환합니다.
    # 오류를 정상 성공으로 포장하지 않고 해당 원인에서 중단합니다.
    doc=by_doc(doc_id)  # 주어진 ID에 해당하는 원본 문서를 찾습니다.
    parsed=parse_one(doc)  # 문서 본문을 파싱해 인덱싱할 수 있는 단위로 나눕니다.
    if parsed['status']!='parsed':raise ValueError('not indexable')  # 파싱이 성공하지 않으면 원인을 알리며 중단합니다.
    chunks=make_chunks(doc,parsed['units'][0],size=110,overlap=15)  # 첫 파싱 단위를 110자 크기, 15자 겹침으로 청킹합니다.
    first=chunks[0]  # 검사와 반환에 사용할 첫 번째 청크를 선택합니다.
    if not first['body'].strip() or not first['embedding_text'].startswith('passage: '):  # 본문이 비었거나 E5 접두사가 없으면 유효하지 않습니다.
        raise ValueError('bad embedding input')  # 잘못된 임베딩 입력을 정상 데이터처럼 사용하지 않도록 오류를 냅니다.
    return doc,first  # 원본 문서와 검증한 첫 청크를 함께 반환합니다.
    # END D24-07-B01


def format_hit(row:tuple)->dict:  # DB 검색 결과 한 행을 일관된 딕셔너리로 변환합니다.
    """DB 행: citation_id,chunk_id,body,locator,doc_id,version,distance."""  # DB 결과 튜플의 필드 순서를 설명합니다.
    # BEGIN D24-07-B02
    # 개념·실무 해설: 실제 DB가 발급한 citation_id는 양의 정수입니다. 반환 튜플의 필드 순서를 원문·출처·거리와 함께 명시적으로 매핑합니다.
    # 해설 D24-07-B02 : DB 검색 결과 행을 정수 citation_id·chunk_id·본문·출처·거리의 딕셔너리로 변환합니다.
    # 입력·출력은 함수 시그니처와 docstring에 따릅니다.
    # 이 블록은 예제를 따라 실행하며 검증 가능한 결과를 반환합니다.
    # 오류를 정상 성공으로 포장하지 않고 해당 원인에서 중단합니다.
    cid,chunk_id,body,locator,doc_id,source_version,distance=row  # DB 행을 약속된 순서대로 변수에 풀어 담습니다.
    if type(cid) is not int or cid<=0:raise ValueError('invalid citation ID')  # citation ID가 양의 정수가 아니면 오류를 냅니다.
    return {'citation_id':cid,'chunk_id':chunk_id,'body':body,  # 인용 ID, 청크 ID, 본문을 결과에 담습니다.
            'source_locator':locator,'doc_id':doc_id,  # 출처 위치와 문서 ID를 결과에 담습니다.
            'source_version':source_version,'cosine_distance':float(distance)}  # 버전과 거리를 담고 거리는 실수형으로 변환합니다.
    # END D24-07-B02


def main():  # 기본 실행과 선택적 실DB 실행의 전체 순서를 담당합니다.
    doc,chunk=select_index_chunk('DOC-ASSIGN')  # 실습 문서에서 인덱싱에 쓸 문서와 청크를 가져옵니다.
    output={'source_mode':'prepared_only_not_db','chunk':chunk,  # 기본 실행은 DB 미사용 상태와 대상 청크를 기록합니다.
            'live_db':'not_run','sample_hit_contract':format_hit((201,chunk['chunk_id'],chunk['body'],chunk['source_locator'],doc['doc_id'],'v1',0.0))}  # 결과 형식 예시를 만들어 출력에 포함합니다.
    if '--live-db' in sys.argv:  # 명령줄에 --live-db가 있을 때만 실제 모델과 DB를 사용합니다.
        from coursekit.live import connect_db,load_encoder,encode_passages,encode_query  # DB 연결과 E5 모델·임베딩 함수를 가져옵니다.
        from coursekit.db import initialize,stage_version,publish_version,search_current,use_schema  # 스키마 설정, 적재, 게시, 검색 함수를 가져옵니다.
        # 실제 모델 추론은 DB 트랜잭션 전에 수행합니다.
        model=load_encoder();vectors=encode_passages(model,[chunk])  # E5 모델을 불러오고 청크의 passage 임베딩을 계산합니다.
        query=encode_query(model,'과제 파일은 어디에 보관하나요?')  # 예시 질문을 E5 query 임베딩으로 변환합니다.
        with connect_db() as conn:  # 설정된 PostgreSQL DB에 연결하고 블록 종료 시 연결을 정리합니다.
            use_schema(conn,'d24_basic07')  # 수업 전용 스키마를 현재 연결의 검색 경로로 지정합니다.
            initialize(conn)  # 필요한 수업용 테이블과 인덱스를 준비합니다.
            with conn.transaction():  # 청크 적재와 버전 게시를 하나의 트랜잭션으로 처리합니다.
                stage_version(conn,doc,doc['file'],[chunk],vectors)  # 문서 청크와 계산한 벡터를 새 버전으로 저장합니다.
                publish_version(conn,doc['doc_id'],doc['source_version'],chunk['pipeline_version'])  # 저장한 문서 버전을 현재 버전으로 게시합니다.
            result=search_current(conn,query,category='학사',k=3)  # 학사 범주에서 질문과 가까운 결과 최대 3개를 검색합니다.
            output['source_mode']='e5_pgvector_live'  # 실제 E5와 pgvector를 사용한 실행 모드임을 표시합니다.
            output['live_db']=[format_hit(r) for r in result]  # 검색 행마다 출력 형식 변환을 적용합니다.
    out=save_json(HERE,'indexing.json',output)  # 실행 결과를 현재 폴더의 indexing.json에 저장합니다.
    show_success('07 Basic',out)  # 저장 성공 안내와 결과 파일 위치를 출력합니다.

if __name__=='__main__':main()  # 이 파일을 직접 실행했을 때만 main 함수를 호출합니다.
