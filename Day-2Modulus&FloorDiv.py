# # # Day 2	Modulus & Floor Div	Batch processing	Even/odd, cycles

# # # chocolates = 10
# # # box_size = 3
# # # full_boxes = chocolates // box_size
# # # print(full_boxes)   # → 3

# # # chocolates = 10
# # # box_size = 3
# # # full_boxes = chocolates /box_size
# # # print(full_boxes)   # → 3.3333333333333335

# # # chocolates = 7
# # # # box_size = 3
# # # # full_boxes = chocolates // box_size
# # # # print(full_boxes)

# # # # chocolates = 11
# # # # box_size = 4
# # # # full_boxes = chocolates // box_size
# # # # leftover = chocolates % box_size
# # # # print(full_boxes)   # should be 2
# # # # print(leftover)      # should be 3


# # # Level 1 — Foundation (4 Questions)

# # # You have 50 rows and box size 6. How many full boxes, and how many leftover? (reason first, then code)
# # # 100 // 7 — work out the answer by hand first, then confirm in code.
# # # 100 % 7 — using the same numbers, work out the leftover by hand, then confirm in code.
# # # 2 ** 5 — what does this mean step by step (not just the answer)? Write it out as repeated multiplication, then confirm in code.


# # # Level 2 — Applied to Pipelines (4 Questions)

# # # Nielsen pipeline has 83,000,000 rows, batch size 10,000,000. How many complete batches run, and how many rows are leftover for the next run?
# # # Row number 4,500 — is it even or odd? Use modulus to prove it (what's the rule for even/odd using %?).
# # # A dataset doubles every year, starting at 5,000 rows. How many rows after 6 years? (use **)
# # # A pipeline has 145,000 rows, batch size 20,000. After running all complete batches, how many rows are left for a final smaller batch?


# # # Level 3 — Interview-Style Reasoning (2 Questions)

# # # A colleague says: "I used // to report pipeline completion percentage to a client." Explain why this is the wrong tool, and what should be used instead. (Connect this to what you just learned about // hiding leftover detail.)
# # # True or False: "17 // 5 and 17 % 5 will always add up to 17 if you reverse the math (i.e., (17 // 5) * 5 + (17 % 5) equals 17)." Try it with your own numbers first, then explain why this relationship makes sense — what does // and % each represent in this equation?



# # # Q1. You have 37 rows to process, and each batch can hold 8 rows. How many complete batches can you run?
# # total_rows = 37
# # batch_hold_rows = 8 

# # total_batch = total_rows // batch_hold_rows
# # print(total_batch)

# # # Q2. A server can handle 6 parallel jobs at a time. You have 50 pending jobs in queue. How many full rounds of 6 jobs can be dispatched at once?


# # total_pending_jobs = 50
# # Server_capacity = 6 
# # total_dispatched = total_pending_jobs // Server_capacity
# # print(total_dispatched)

# # leftover = 37 % 8
# # print(leftover)

# # Q1. 50 pending jobs, server handles 6 at a time (same as before). You already know 8 full rounds dispatch. How many jobs are leftover, unable to fill a 9th round? Reason it out, then confirm with 50 % 6.
# leftover = 50 %6
# print(leftover) #2

# # # Q2. A pipeline has 145,000 rows, batch size 20,000. Using both // and %, find: how many complete batches, and how many rows leftover for a final smaller batch?
# pipeline_rows = 145000
# batch_size = 20000

# total_batch_count = pipeline_rows // batch_size
# print(total_batch_count) # answer = 7 

# total_batch_count = pipeline_rows % batch_size
# print(total_batch_count) # answer = 5000

# ex = 2 ** 276
# print(ex) #121416805764108066932466369176469931665150427440758720078238275608681517825325531136


# # A table starts with 1,000 rows and doubles every year. How many rows will it have after 5 years?

# # rows = 1000
# # tune = 5 
# # every_year = 2 

# # total = tune ** every_year
# # print(total)

# # rows = 1000
# # years = 5
# # doubling_factor = 2 ** years        # 32
# # total_rows = rows * doubling_factor  # 1000 * 32
# # print(total_rows)



# # Q1. 4 ** 3 — work it out by hand as repeated multiplication first, then confirm in code.
# # 12 - is answer
# # Q2. A dataset starts at 500 rows and doubles every month. How many rows after 4 months?

# start_rows = 500
# double_effects =  2 
# Months = 4
# double_effects =  2 ** Months # this will return as total times of double 

# # print(double_effects) #16

# Total = double_effects * start_rows
# print(Total) # is the answer 8000 
# # Q3. A server's storage cost triples every year (multiply by 3, not 2). Starting cost is ₹2,000/year. What's the cost after 3 years?
# starting_cost = 2000
# multiply_cost_yeraly = 3
# forecasting_cost_after3years = 3 

# #first we will find out the how much multiply then we will multiply with the this numbers with the total cost

# multiply = multiply_cost_yeraly ** forecasting_cost_after3years
# #print(multiply) #27 

# total = starting_cost * multiply
# print(total) #54000( this is not an real logic. )

# # Q4. You're told an algorithm's time complexity is 2^n. If n = 10 (10 input items), how many operations does that represent? (Just calculate 2 ** 10 and think of it as "operation count.")
# # i dont understand this question
# # Q5. A pipeline's error rate halves every week (this is tricky — halving is NOT the same as doubling). Starting error count is 800 errors. 
# After 3 weeks of halving, how many errors remain? (Hint: think about whether ** alone solves this, or if you need a different approach — try it and see what happens.)
# # not understanding this question. 


# Q1. A cloud storage bill starts at ₹5,000/month and
# increases by a factor of 2 (doubles) every 6 months. 
# What's the bill after 3 doubling periods (i.e., 18 months)?

# var = 18 // 6
# print (var) # 3 

# cloud_storage_per_month_bills = 5000 
# doubles_factor = 3 # how much time will double in the 18 months, finally I got
# Months = 18

# total= doubles_factor ** Months
# print(total) # 387420489

# final = cloud_storage_per_month_bills * total
# print(final) 1937102445000


# Q1. Something doubles, 4 times. Starting value is 100.

# Step 1: find the growth multiplier (2 ** how many times?)
# m = 2 ** 4 
# # print(m) answer = 16 times the answer 
# # Step 2: multiply by starting value
# p = 100 * m
# print(p)
# Q2. Something triples, 2 times. Starting value is 50.
# v = 3 ** 2 
# # print(v)
# value = 50 * v
# print(value)
# # Q3. Something doubles, 5 times. Starting value is 10.
# double = 2 ** 5 
# print(double)
# # answer is 32
# final = 10 * double
# print(final)
# Q4. Something quadruples (×4), 3 times. Starting value is 1000.
# a = 4 ** 3 
#Q2. A server cost starts at ₹12,000/month and triples every 2 months. After 8 months, what's the cost?
# cost_montly = 12000
# reperated = 3 
# nowwewillfindoutthehowmanytriplesin8months = 8 // 2
# # print(nowwewillfindoutthehowmanytriplesin8months) #4 now this 4 will exponset with 3 times because every month2 month will reachout to afrre 4 times then 8 will reac
# values = 3**4 
# final = cost_montly * values
# print(final) #972000 value = 1000 * a 
# # print(value)

# Q5. Something doubles, 6 times. Starting value is 1.
# doubles = 2 ** 6 
# value = 1 * doubles
# print(value)



# # Q1. A dataset starts at 2,000 rows and triples every 6 months. After 18 months, 
# # how many rows?

# how_manytimesof_repeted = 3
# now_wewillfigureout_in18month_splitintohow_many6monthswillcome = 18 // 6
# wegoit3so = 3 # we got periodic 
# total_rows = 2000

# sonow= how_manytimesof_repeted ** wegoit3so

# value_final = sonow * total_rows
# print(value_final)



# Q1. A pipeline starts at 50,000 rows and doubles every 3 days. problem statement : After 15 days, how many rows?

# rows = 50000
# reperated  = 2 
# Now_iwillfigureout15days_inevery3days = 15 // 3
# print(Now_iwillfigureout15days_inevery3days) #we got answer 5 so  what is the 5, 5 is nothing but this is we calcluated like 3,3,3,3,3 that day we calculated with given days 3, then the mulply output came
# #then that multyply help to expontial the with repearted
# sonowwewillfindthehowmanytimeswilldobuletherowsinafter15days = 2 **5 
# final = rows * sonowwewillfindthehowmanytimeswilldobuletherowsinafter15days
# print(final) #1600000

# 

# Q3. A dataset starts at 100,000 records and quadruples every 5 days. After 20 days, how many records?
# records = 100000
# repearted = 4 
# nowwewillfindouttogthe = 20 // 5 
# values = repearted ** nowwewillfindouttogthe
# final = records * values
# print(final)
# answer = 25600000

# Q4. A cloud bill starts at ₹25,000 and doubles every 3 months. After 12 months, what's the bill?
# Bills = 25000
# repeted = 2 
# nowima = 12 // 3 
# values = repeted ** nowima
# final = values * Bills
# print(final) #400000

# Q5. A user base starts at 8,000 users and triples every 4 weeks. After 16 weeks, how many users?
# rows_base_starts = 8000
# repeted = 3 
# nowmai = 16 // 4 
# values = repeted ** nowmai
# final = rows_base_starts * values
# print(final) # 648000



































# Q2. A server cost starts at ₹800/day and doubles every 4 days. After 20 days, what's the cost?

# Level B — Combining exponents with something else you already know (subtraction or comparison)
# Q3. Pipeline A starts at 1,000 rows and doubles every year for 4 years. Pipeline B starts at 5,000 rows and stays flat (no growth). After 4 years, which pipeline has more rows, and by how much?
# Q4. A cost starts at ₹1,000 and triples every year for 3 years. What's the total increase (not the final amount — the difference between final and starting)?

# Level C — Reverse thinking (harder — given the final answer, work backward)
# Q5. Something doubles a certain number of times, starting from 5, and ends at 320. How many times did it double? (Hint: you may need to try a few values of "times" and check which one gives 320 — or think about it as "5 × 2^? = 320", what's "?")


