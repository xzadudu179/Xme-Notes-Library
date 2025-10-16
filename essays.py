from datetime import datetime
import sys
from zoneinfo import ZoneInfo

def main(args):
    with open("./source/_data/essays.yml", 'a', encoding='utf-8') as file:
        content = (''.join(args)).replace('\n', '\n    ')
        file.write(f"- content: |\n    {content}\n  date: {datetime.now(tz=ZoneInfo('GMT')).strftime('%Y-%m-%d %H:%M:%S')}\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        lines = []
        print("请输入说说吧(/end 结尾)")
        while True:
            line = input(">")
            if line == "/end":
                break
            lines.append(line)
        main('\n'.join(lines))