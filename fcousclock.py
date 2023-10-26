import time

def focus_timer(work_minutes, break_minutes):
    while True:
        # 专注工作阶段
        print(f"专注时间: {work_minutes} 分钟")
        time.sleep(work_minutes * 60)

        # 休息阶段
        print(f"休息时间: {break_minutes} 分钟")
        time.sleep(break_minutes * 60)

if __name__ == "__main__":
    work_minutes = 25  # 设置专注工作时长（以分钟为单位）
    break_minutes = 5  # 设置休息时长（以分钟为单位）
    focus_timer(work_minutes, break_minutes)
