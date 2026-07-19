# # # # # Day 1: Numbers & Basic Arithmetic

# # # # # The foundation of everything in DE & DSA

# # # # # 🤔 Why This Day Matters
# # # # # Every pipeline counts rows, calculates revenue, measures time. Without arithmetic — no pipeline works!

# # # # # 🏭 Real Life DE Example
# # # # # You have 83 Million rows in Nielsen pipeline. You loaded 80M. How many remaining? How much % complete?

# # # # total_row_count = 83000000
# # # # row_processed = 80000000
# # # # remaining_left = (total_row_count - row_processed)
# # # # print(remaining_left) #30,000,000

# # # # Per = (remaining_left / total_row_count)*100
# # # # print(Per)
# # # # per2 = (row_processed / total_row_count) * 100
# # # # print(per2)


# # # # 1. Multiplication — the remaining Day 1 practice questions:
# # # # Q2: Each batch processes 10,000 rows. Revenue per row = ₹5. Total revenue?
# # # Total_Batch_rows = 10000
# # # Revenue_per_row = 5
# # # total_Revenue = (Total_Batch_rows * Revenue_per_row)
# # # print(total_Revenue)

# # # # Q3: Pipeline runs 3.5 hours per day for 5 days. Total hours?

# # # Total_day= 5 
# # # Pipeline_runes_perday_hr = 3.5
# # # total_pipelineruns_count = Total_day * Pipeline_runes_perday_hr
# # # print(total_pipelineruns_count)

# # # a = 10
# # # b = 2
# # # print(type(a / b))   # → 5.0, NOT 5  (still a float, even though it divides evenly!)

# # # A = 10
# # # B = 3
# # # print(type(A / B)) 

# # # # 2. Two interview questions — answer in your own words (no code):

# # # # What is the difference between int and float in Python?
# # # # int - store the holl number 
# # # # and float store the decimal numbers in python, and as per the data engineering aspect rows count alwsys
# # # # int count
# # # # # What happens when you divide two integers in Python 3?
# # # # any numbers can comeup on the output depends on tyhe numbers we're print
# # # # a = 11
# # # # b = 10
# # # # x = a / b
# # # # print(x)

# # # # #1. Addition (+) — Combining
# # # # #The concept: nothing is lost or removed — I am just merging quantities.
# # # # total_row_count_looaded_yesterday = 80000000
# # # # total_row_count_looaded_today = 3000000
# # # # total_rows_loaded = (total_row_count_looaded_yesterday + total_row_count_looaded_today)
# # # # print(total_rows_loaded)



# # # # # 2. Subtraction (−) — Finding the gap or what's left
# # # # # The concept: you're measuring a difference between two amounts.
# # # # Total_rows = 83000000
# # # # total_row_count_looaded_yesterday = 70000000
# # # # total_row_count_looaded_today = 3000000
# # # # total_rows_loaded = total_row_count_looaded_yesterday + total_row_count_looaded_today

# # # # diffrent = Total_rows - total_rows_loaded
# # # # print(diffrent)

# # # # # 3. Multiplication (×) — Repeated addition, or scaling

# # # # units_sold = 1000
# # # # per_unit_revenue = 500

# # # # total_revenue_of_unit_sold = units_sold * per_unit_revenue
# # # # print(total_revenue_of_unit_sold)


# # # # # 4. Division (÷) — Splitting into equal parts

# # # 🎉 Day 1 — Complete
# # # Here's what you actually built today, not just "did":

# # # ✅ Understand int vs float, and why DE treats counts vs measurements differently
# # # ✅ All 4 basic operations, with real pipeline reasoning behind each
# # # ✅ Caught your own / vs % confusion and fixed it — that's a real engineer instinct
# # # ✅ Caught a >100% red flag on your own logic and corrected it
# # # ✅ Proved percentage math using two different methods that matched
# # # ✅ Can state the "Python 3 division always returns float" rule from first principles, not memorization

# # candies = 10 
# # frinds = 3 
# # each_frinds = candies / frinds
# # print(each_frinds)

# # candies = 10 
# # frinds = 3 
# # each_frinds = candies % frinds
# # print(each_frinds)

# # can = 17
# # frin = 5
# # each = 


# # 1. I have 83,000,000 total rows. 79,000,000 are processed. Write the code to find:

# # How many rows remain
# # What % is remaining
# # What % is complete

# # total_rows = 83000000 
# # processed_rows = 79000000
# # complete_rows = processed_rows / total_rows * 100
# # print(complete_rows) #95.18072289156626 rows has been processed / completed

# # remaining = processed_rows + total_rows * 100
# # print(remaining)

# total_rows = 83000000
# processed_rows = 79000000

# remaining_rows = total_rows - processed_rows
# print(remaining_rows)

# percent_remaining = (remaining_rows / total_rows) * 100
# print(percent_remaining)

# # 2. Quick reasoning (no code, just answer in words): what's the actual difference between what / and % tell you? Use any example you like — candies, rows, anything.
# # 3. True or false, and why: 10 / 5 in Python gives you 2 (a plain integer).




# # Q1: You have 83M rows. Loaded 75M. How many remaining? Write in Python.
# # rows = 83
# # loadded = 75 
# # total = rows - loadded
# # # print(rows)
# # # • Q2: Each batch processes 10000 rows. Revenue per row = ₹5. Total revenue?
# # batch_process = 10000
# # per_rows = 5 
# # total = batch_process * per_rows
# # print(total)
# # # • Q3: Pipeline runs 3.5 hours per day for 5 days. Total hours?

# # pipeline_runs_day = 3.5
# # total_day_runs = 5

# # total_hours_runs = pipeline_runs_day *  total_day_runs
# # print(total_hours_runs)

# # if i will run = 
# # total_hours_runs =  total_day_runs * pipeline_runs_day




