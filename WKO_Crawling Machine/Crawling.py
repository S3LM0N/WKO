from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":
"반려견 치와와, 반려견 말티즈, 반려견 미니어처 핀셔, 반려견 파피용, 반려견 포메라니안, 반려견 푸들, 반려견 시추, 반려견 미니어처 슈나이저, 반려견 요크셔 테리어, 반려견 에어데일 테리어, 반려견 스코티시 테리어, 반려견 비글, 반려견 닥스훈트, 반려견 아프간 하운드, 반려견 그레이 하운드, 반려견 바셋 하운드, 반려견 코커스페니얼, 반려견 골든 리트리버, 반려견 포인터, 반려견 세터, 반려견 비즐라, 반려견 시베리안 허스키, 반려견 알래스칸 말라뮤트, 반려견 도베르만 핀셔, 반려견 로트 와일러, 반려견 버니즈 마운틴독, 반려견 보더콜리, 반려견 셔틀랜드 쉽독, 반려견 웰시코기, 반려견 저먼 셰퍼드, 반려견 올드 잉글리시 쉽독, 반려견 러프콜리, 반려견 진돗개, 반려견 삽살개, 반려견 풍산개, 반려견 불독, 반려견 시바견, 반려견 달마시안, 반려견 비숑프리제, 반려견 차우차우 "
    ,"limit":100,"print_urls":True, "format": "jpg"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images