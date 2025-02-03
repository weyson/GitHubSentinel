import feedparser
import os
from datetime import datetime, date, timedelta  # 导入日期处理模块
from logger import LOG  # 导入日志记录器

# rss_url = 'https://hnrss.org/best'

class HackerNewsClient:
    def __init__(self):
        self.rss_url = 'https://hnrss.org/best'

    def get_best_news(self):
        LOG.info('开始获取best hacker news')
        xml_data = feedparser.parse(self.rss_url)
        for news_data in xml_data.entries:
            title = news_data['title']
            print(f'title: {title}')
            published = news_data['published']
            print(f'published: {published}')
            summary = news_data['summary']
            print(f'summary: {summary}')

        LOG.info('结束best hacker news')

    def export_daily_progress(self):
        LOG.debug(f"[准备导出项目进度]：Hacker News")
        today = datetime.now().date().isoformat()  # 获取今天的日期
        repo_dir = os.path.join('daily_progress', 'hacker_news')  # 构建存储路径
        os.makedirs(repo_dir, exist_ok=True)  # 确保目录存在

        xml_data = feedparser.parse(self.rss_url)
        file_path = os.path.join(repo_dir, f'{today}.md')  # 构建文件路径
        count = 0
        with open(file_path, 'w') as file:
            file.write(f"# Daily Progress for Hacker News ({today})\n\n")
            for news_data in xml_data.entries:
                if count > 5:
                    break

                count = count + 1
                title = news_data['title']
                published = news_data['published']
                summary = news_data['summary']
                file.write(f'# {title}\n')
                file.write(f'- {published}\n')
                file.write(f'- summary: {summary}\n\n')

        LOG.info(f"[Hacker News]项目每日进展文件生成： {file_path}")  # 记录日志
        return file_path