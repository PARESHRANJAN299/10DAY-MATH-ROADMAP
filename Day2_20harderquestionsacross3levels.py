# Level 1 — Harder Foundation (7 Questions)

# 237 // 15 and 237 % 15 — calculate both, then verify: does (237 // 15) * 15 + (237 % 15) equal 237?
# A pipeline processes rows in batches of 12,000. Total rows = 145,750. How many complete batches, and how many leftover rows?
# 5 ** 4 — work it out by hand (5×5×5×5) before running code.
# Row number 78,653 — even or odd? Prove it with %.
# A number, when divided by 9, leaves remainder 0. What does that tell you about the number? Give 2 example numbers that satisfy this.
# 100000 // 3 vs 100000 % 3 — calculate both. Which one tells you "how many groups," and which tells you "what's left"?
# A batch size is 7,500. A pipeline has processed 202,500 rows exactly. How many complete batches ran? Any leftover?


# Level 2 — Applied, Multi-step (7 Questions)

# A dataset starts at 3,000 rows and doubles every 5 days. After 30 days, how many rows?
# Two pipelines: Pipeline A starts at 10,000 rows, triples every 3 months, for 9 months. Pipeline B starts at 500,000 rows and stays flat. After 9 months, which has more, and by how much?
# A server fleet starts at 4 servers and quadruples every quarter, for 2 quarters. Storage cost is ₹500/server/month. What's the total monthly storage cost after those 2 quarters?
# A pipeline has 83,000,000 rows, batch size 6,000,000. Find complete batches AND leftover rows. Then find what % of total rows the leftover represents.
# A number doubles every week for 4 weeks, reaching 1,600. What was the starting number? (Work backward — find 1600 / (2**4).)
# A cost triples every 2 years for 6 years total, ending at ₹98,415,000. What was the starting cost? (Reverse the growth calculation.)
# A batch job runs every 6 hours. If a pipeline started at midnight (hour 0) and it's now hour 134, how many complete batch cycles have run, and how many hours into the current cycle are we?


# Level 3 — Interview-Style Reasoning & Edge Cases (6 Questions)

# A colleague writes growth = starting_value ** periods to calculate compound growth (e.g., doubling). Explain exactly why this is structurally wrong, using the "what repeats" rule.
# True or False: "// and % will always give the same numeric result if the total number is exactly divisible by the divisor." Explain with an example.
# A pipeline dashboard shows a dataset "growing by 1600x" over some period, but the engineer can't remember how many doubling periods that represents. Given 1600x isn't a clean power of 2, what does that suggest about the growth pattern (is it possibly NOT simple doubling)?
# Explain, in your own words, why exponents are relevant to "Big O" thinking in interviews — connect it to the fact that 2**n grows extremely fast as n increases. Try comparing 2**10 vs 2**20 to make the point concrete.
# A junior engineer calculates % of rows processed using (processed_rows // total_rows) * 100 instead of (processed_rows / total_rows) * 100. Predict what will happen for most real pipeline numbers (hint: think about what // gives you when the numerator is smaller than the denominator).
# Design a mental checklist (3-4 steps) you would personally use to avoid ever mixing up base/exponent again — write it in your own words, as if creating a rule for yourself to follow permanently.


# # 🎯 Practice Questions
# # • Q1: 83000000 rows, batch size 50000. How many complete batches? Any leftover?

# row = 83000000
# batch_size = 50000

# total_batchs = row // batch_size
# # print(total_batchs) 1660 total Bacth Size
# total_batchs = row / batch_size
# print(total_batchs) #1660.0  nothing is the left over. 

# • Q2: Is row number 4500 even or odd? Use modulus!

# row_number  = 4500
# check = 2 

# value = row_number % check
# print(value) #0 is the output so the 4500 is the even 

# • Q3: A table doubles every year. Starts at 1000 rows. Size after 5 years?

# start_rows = 1000 
# rowswilldoubleineveryyeras = 2  
# time = 5 

# howmuchcount= start_rows ** rowswilldoubleineveryyeras
# print(howmuchcount) #1000000 i got the total count 

# final_size = howmuchcount * 5
# # print(final_size) answer = 5000000 after 5 years row count will be 


# Q1: A Databricks job starts with 200 rows. It triples every day. How many rows after 3 days?
# rows_start = 200
# doubleing_factor = 3
# exponets = 3

# total= rows_start * (doubleing_factor ** exponets)
# print(total)

# # one more option to find the answer 
# a = doubleing_factor ** exponets
# totAL = a * rows_start
# print(totAL)
# # Q2: You have 91,000,000 rows to load, in batches of 7000. How many complete batches, and how many rows leftover?
# rows_load = 9100000
# one_batch = 7000

# overal = rows_load / one_batch
# print(overal) #1300.0 total batch and there are no leftover 

# Q3: A subscription table has 6400 rows. It halves every year (due to churn/cleanup). How many rows after 4 years?

# sub_table_rows = 6400

# leftover = 2
# Exception_year = 4

# total = sub_table_rows / Exception_year
# print(total)


# # Q: A Nielsen data file starts at 2 GB. Due to a bug, its size doubles every week it goes unfixed. If it goes unfixed for 6 weeks, what's the file size?
# file_starts = 2 
# double_factor = 2
# Exception_files = 6 

# total = Exception_files ** double_factor
# print(total)


# # Quick check for you: if a job runs 3 weeks, how many days is that? Just say the number.

# job_runs_weeks  = 3 
# one_week_days = 7

# totol_days_runs = job_runs_weeks * one_week_days
# print(totol_days_runs) # answer is 21 days is will take. 

# #  so i am creating question myself 
# # if a job run 3 weeks then how many mins total runs ? 
# job_runs_weeks  = 3 

# # now i will convert the total mins of weekly 

# hours = 60
# one_day_total_hours = 24
# one_week = 7


# # then we will find the in a day total of mins
# total_mins_per_day = hours * one_day_total_hours
# print(total_mins_per_day) # 1440 per days. 
# # now we will find the weekly total how many mins
# Total_mins_per_week = total_mins_per_day * one_week
# # print(Total_mins_per_week) #10080
# # now we find the total weekly mins
# # now we will conver this into 3 weeks 
# final_mins_count = Total_mins_per_week * job_runs_weeks
# print(final_mins_count) # 30240 yes done. 



# Q1 (Exponential growth): A log table starts at 500 rows. It doubles every day. Size after 7 days?
 
# table_rows = 500
# double_factor = 2 
# Exception_data = 7 

# total = double_factor ** Exception_data
# new = total * table_rows
# print(new)

# Q2 (Exponential decay): A cache has 8000 entries. It shrinks to half every hour due to expiry. How many entries after 5 hours?
# entries = 8000
# based_expiry = 0.5
# exponantial = 5 
# # What is the count of every hour
# exponantial_hour = 1 
# final_value = entries * (based_expiry**exponantial_hour)
# print(final_value) #4000.0
# # so then i will count for 5 hours myself
# total_entries_count = based_expiry ** exponantial
# final_ouput = total_entries_count * entries
# print(final_ouput) #250.0

# # Q3 (Conversion): A pipeline runs every 15 minutes. How many times does it run in a single day (24 hours)?
# pipeline_runs = 15  #every 15 mins

# # so we will calculate how many times will run in every hour , and here mins is the base key

# # # 1 hours = 60 mins
# # hours_1 = 60

# # total_runs_mins_runsper_hour = hours_1 // pipeline_runs
# # print(total_runs_mins_runsper_hour) # the answer is 4 

# # # so now we will find this one 24hours. 
# # # we will convert 24 hours is how many mins
# one_day = 1440
# # hrs = 60
# # one_day_hrs = 24
# # # so then 
# # total_minsone_day = one_day_hrs * hrs
# # print(total_minsone_day ) so one day is 1440 mins 

# # then now we will conver this how nany mins runs the piepie total because we have total mins with us. 

# total_pipeline_runs = one_day // pipeline_runs
# # print(total_pipeline_runs) so the answer is pipeline total runs 96 times. 

# Q4 (Exponential growth): A Walmart product catalog starts with 100 SKUs. It triples every quarter. How many SKUs after 3 quarters?

# SKU = 100
# double_factor_on_qa = 3 

# BaseException_onSKU_qa = 3

# total = SKU * (double_factor_on_qa ** BaseException_onSKU_qa)
# # print(total) 2700 is the answer

# # Q5 (Conversion): A job takes 90 seconds to run. How many minutes is that?
# a_job_take_to_run = 90 
# # first don't know 1 mins is how many secancds 

# frist_1_mins = 1

# total_mins = a_job_take_to_run % frist_1_mins
# print(total_mins)  #so the leftover is 0 , that menas 1 mins is 90 secn. and the pipeline take 1 mins to run. 

# # Q6 (Exponential decay): A subscription has 50,000 active users. It drops to 70% (multiply by 0.7) every month due to churn. How many users after 3 months? 

# subscription_active_users = 50000
# Months_drops = 0.7
# exponantial_months = 3 

# # total = subscription_active_users  * (Months_drops ** exponantial_months)
# # # print(total) 17149.999999999996

# # # then in the first months this will drop to 
# # exponantial_months_1 = 1 

# # totala = subscription_active_users  * (Months_drops ** exponantial_months_1)
# # print(totala) #35000.0 will be active subscribe will be available 

# # # Q7 (Conversion): A batch job is scheduled every 4 hours. How many times does it run in a full week?

# # batch_scheduled_every_hours = 4 

# # fullWeek = 7

# # # # but first i will find in one day how many times will my pipeline will run 
# # # one_day_hours = 24
# # # total_pipeline_runs = one_day_hours //batch_scheduled_every_hours
# # # print(total_pipeline_runs) #6 so then in one day 6 times will run my pipeline 

# # # then in a week 
# # will run 

# variable = 6 *7 
# # print(variable)42 times will run my pipeline. 


# # Q8 (Exponential growth): A MARS sales data file starts at 5 MB. It doubles every day due to a duplicate-write bug. Size after 10 days?

# startwith_datainMB = 5 

# double_factor = 2 
# exponsenatioal = 10 

# total = startwith_datainMB *(double_factor**exponsenatioal)
# print(total) 5120 total 
# # Q9 (Conversion): A Nielsen period covers 4 weeks. How many total hours is that?
# period_coverweeks  = 4 

# total_hours = "?"

# # first i will find one one week is how many hours

# one_week_days = 7 

# one_day_hours  = 24

# total_hoursinweek = one_week_days * one_day_hours
# # print(total_hoursinweek) 168 hours one week. 
# # so now we will conver this 
# four_week_total_hours = total_hoursinweek * period_coverweeks
# print(four_week_total_hours)
# # answer is 672hours in a week. 

# varibale = 7 * 24
# print(varibale)
# total_hours_inweek=  168
# final = total_hours_inweek * 4
# print(final)

# # Q10 (Mixed — growth + conversion): A queue starts with 10 messages. It triples every hour. 
# # After converting 2 days into hours, 
# # how many messages are in the queue at the end of day 2?


# queue_start_with = 10
# double_factor = 3 
# exponantial_days = 2 

# final = queue_start_with *(double_factor **  exponantial_days)
# print(final)