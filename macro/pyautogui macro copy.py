import pyautogui as pag  # <--pyautogui를 줄여서 사용하겠다
import time
login_btn = pag.position(x=906, y=424)
pag.click(login_btn) #로그인 창 띄우기
id_btn = pag.position(x=432, y=364)

my_id = "****" #id 
my_pw = "****" #pw

pag.typewrite(my_id,interval=0.5)
pag.press("tab")
pag.typewrite(my_pw,interval=0.2)

login_final = pag.position(x=501, y=525)
pag.click(login_final)



#마우스,키보드 좌표로 매크로 만들기
#네이버 로그인 하기 실패. 자동입력 방지가 걸린다 방법이 없을까? 
# pag.time.sleep()
# pag.typewrite(my_id,interval=1) interval로 입력시간 늘리기