number = int(input())
hours = number // 3600
minutes = (number - (number // 3600) * 3600) // 60
seconds = (number - ((number // 3600) * 3600) - ((number - (number // 3600) * 3600) // 60) * 60)
print(f"{hours:02}:{minutes:02}:{seconds:02}")