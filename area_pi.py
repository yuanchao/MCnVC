import random

m_total = 10**5
m_radius = 1

def in_circle(point):
    x = point[0]
    y = point[1]
    return (x**2 + y**2) < m_radius**2

m_count = m_inside = 0

for i in range(m_total):
    point = random.random()*m_radius, random.random()*m_radius
    if in_circle(point):
        m_inside += 1
    m_count += 1

pi = (m_inside * 1.0 / m_count) * 4

print(pi)
