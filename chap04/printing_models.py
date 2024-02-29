#출력할 디잔이 저장된 리스트
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs, completed_models):
# 남을 게 없ㅇ르 때 깢 ㅣ디자인 출력
# 출력한 디자인을 컴플리트 모델로 옮깁니다
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model : {current_design}")
        completed_models.append(current_design)

# 완료된 디자인을 표시합니다
def show_completed_models(completed_models):
    print("\n The following models hav been printed:")
    for completed_model in completed_models:
        print(completed_model)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

def modify_string(s) : # 스트 링 값을 전달받음
    s = s + "world" #변수 ssms 원래 변수가 가리키는 주소와 다른 것

st = "hello "
modify_string(st) #출력 결과가 hello
