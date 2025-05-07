import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

# 요리할 음식의 수
num_meals = int(input())
# 각 음식에 필요한 온도 리스트
heat_levels = list(map(int, input().split()))

# 현재 온도에서 목표 온도로 바꾸기 위한 최소 버튼 누름 수 계산
# 순환 구조이기 때문에 양 방향 중 더 짧은 경로 선택
def adjust_button_presses(current_level, target_level):
    return min((current_level - target_level) % 10, (target_level - current_level) % 10)

# 우선순위 큐에 초기 상태 삽입: (총 버튼 누름 수, 현재 음식 인덱스, 왼쪽/가운데/오른쪽 인덕션의 온도)
priority_queue = [(0, 0, 0, 0, 0)]
# 상태별 최소 버튼 누름 수 저장. (음식 인덱스, 인덕션 온도 상태 정렬) -> 최소 누름 수
visited_configurations = defaultdict(lambda: float('inf'))
visited_configurations[(0, 0, 0, 0)] = 0

# Dijkstra 방식으로 탐색
while priority_queue:
    total_presses, meal_idx, left_burner, center_burner, right_burner = heapq.heappop(priority_queue)

    # 모든 음식을 다 요리한 경우 종료
    if meal_idx == num_meals:
        print(total_presses)
        break

    # 현재 음식에 필요한 온도
    required_temp = heat_levels[meal_idx]

    # 각 인덕션 구멍 중 하나를 선택하여 온도를 조절
    for burner_idx, burner_temp in enumerate([left_burner, center_burner, right_burner]):
        # 해당 인덕션을 목표 온도로 바꾸기 위한 버튼 누름 수
        press_count = adjust_button_presses(burner_temp, required_temp)
        # 현재 인덕션 상태 복사 후 해당 구만 온도 변경
        updated_burners = [left_burner, center_burner, right_burner]
        updated_burners[burner_idx] = required_temp
        # 상태 정렬 → 같은 상태로 취급하여 중복 제거
        sorted_burners = tuple(sorted(updated_burners))
        # 다음 음식으로 넘어가는 상태 key
        state_key = (meal_idx + 1, *sorted_burners)
        # 새로운 누름 횟수 계산
        total_cost = total_presses + press_count

        # 해당 상태에서 더 적은 버튼으로 도달 가능하면 갱신
        if visited_configurations[state_key] > total_cost:
            visited_configurations[state_key] = total_cost
            heapq.heappush(priority_queue, (total_cost, meal_idx + 1, *sorted_burners))
