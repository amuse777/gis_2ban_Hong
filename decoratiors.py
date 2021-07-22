# def decorator(func):
#     def decorated(input_text):
#         print('함수 시작')
#         func(input_text)
#         print('함수 끝!')
#     return decorated
#
# @decorator
# def hello_world(input_text):
#     print(input_text)
#
#
# hello_world('Hello_world')


def decorator(func):
    def decorated(hei, based):
        if hei >= 0 and based >= 0:
            return func(hei, based)
        else:
            return ValueError('No!')
    return decorated()


@ decorator
def tri_area(hei, based):
    return hei * based / 2

@ decorator
def squ_area(hei, based):
    return hei * based

tri_area(10, 10)
squ_area(3, 4)
