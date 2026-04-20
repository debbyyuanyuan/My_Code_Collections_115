import MySQLdb
import pandas as pd

# 連線設定（請改成你的密碼）
conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='demo_students', charset='utf8mb4')
# pandas 用 SQLAlchemy 會更方便，但這裡示範用 MySQLdb 與 pandas
sql = """
SELECT e.student_id, s.student_no, s.name, e.subject, e.score, e.exam_date, e.semester
FROM exams e
JOIN students s ON e.student_id = s.id
"""
df = pd.read_sql_query(sql, conn)

# 選擇要處理的學期，例如 '2025S1'
semester = '2025S1'
df_sem = df[df['semester'] == semester].copy()

# 用 pandas 計算每位學生該學期的總分、平均、筆數
summary = df_sem.groupby(['student_id']).agg(
  total_score = ('score', 'sum'),
  avg_score = ('score', 'mean'),
  exams_taken = ('score', 'count')
).reset_index()

summary['avg_score'] = summary['avg_score'].round(2)
summary['semester'] = semester

print(summary)

# 把 summary 寫回 MySQL（使用 INSERT ... ON DUPLICATE KEY UPDATE）
cursor = conn.cursor()
insert_sql = """
INSERT INTO semester_summary (student_id, semester, total_score, avg_score, exams_taken)
VALUES (%s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
 total_score = VALUES(total_score),
 avg_score = VALUES(avg_score),
 exams_taken = VALUES(exams_taken),
 updated_at = CURRENT_TIMESTAMP;
"""

rows = summary[['student_id','semester','total_score','avg_score','exams_taken']].values.tolist()
cursor.executemany(insert_sql, rows)
conn.commit()

# 檢視寫入結果
df_out = pd.read_sql_query("SELECT ss.*, s.student_no, s.name FROM semester_summary ss JOIN students s ON ss.student_id = s.id WHERE ss.semester = %s", conn, params=(semester,))
print(df_out[['student_no','name','semester','total_score','avg_score','exams_taken']])

cursor.close()
conn.close()