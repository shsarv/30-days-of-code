# Enter your code here. Read input from STDIN. Print output to STDOUT
d_a, m_a, y_a = input().split() 
d_e, m_e, y_e = input().split()

res = 0

if int(y_e) > int(y_a): res = 0

elif int(y_e) < int(y_a): res = 10000

elif int(m_e) > int(m_a): res = 0

elif int(m_e) < int(m_a): res = 500 * (int(m_a) - int(m_e))

elif int(d_e) < int(d_a): res = 15 * (int(d_a) - int(d_e))

print(res) 
