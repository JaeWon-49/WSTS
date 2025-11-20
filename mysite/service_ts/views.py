from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import time

def calculate_heavy_load(n):
    """CPU 집약적인 작업: n 이하의 소수 개수를 세는 함수 (의도적인 부하 유발)"""
    count = 0
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count

def home(request):
    """정상 서비스 엔드포인트"""
    return HttpResponse("<h1>웹 서비스가 정상 작동 중입니다. (Django)</h1>", status=200)

def heavy_task(request):
    """CPU 부하 및 서비스 지연을 유발하는 엔드포인트 (장애 상황 재현)"""
    print("--- heavy_task 요청 시작 ---")
    start_time = time.time()
    
    # 높은 값으로 설정하여 CPU에 큰 부하를 줍니다. (장애 조건)
    limit = 5000000
    
    result = calculate_heavy_load(limit)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"소수 계산 완료. 걸린 시간: {elapsed_time:.2f}초")
    print("--- heavy_task 요청 종료 ---")
    
    # 과도한 CPU 사용으로 인해 응답 시간이 길어집니다.
    return JsonResponse({
        "status": "Task Completed",
        "result": f"1부터 {limit}까지의 소수 개수: {result}",
        "time_taken": f"{elapsed_time:.2f} seconds"
    })