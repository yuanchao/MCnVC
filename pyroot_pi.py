import random
import numpy
import ROOT

m_total = 10**5
m_radius = 1

def in_circle(point):
    x = point[0]
    y = point[1]
    return (x**2 + y**2) < m_radius**2

m_count = m_inside = 0

c1 = ROOT.TCanvas("pi", "#pi", 600, 600)
m_x = numpy.linspace(0, 1.,101)
m_y = (1.**2 - m_x**2)**0.5

c1.cd()

g = ROOT.TGraph(len(m_x), m_x, m_y)
g.SetTitle("#pi")

g.GetXaxis().SetTitle("x")
g.GetYaxis().SetTitle("y")

hist1 = ROOT.TH2F("hist1", "#pi outside", 100, 0, 1, 100, 0, 1)
hist2 = ROOT.TH2F("hist2", "#pi inside", 100, 0, 1, 100, 0, 1)

for i in range(m_total):
    point = random.random()*m_radius, random.random()*m_radius
    if in_circle(point):
        hist2.Fill(point[0], point[1])
        m_inside += 1
    else:
        hist1.Fill(point[0], point[1])
    m_count += 1

pi = (m_inside * 1.0 / m_count) * 4

print(pi)

hist1.SetMarkerColor(4)
hist1.Draw("same")
hist2.SetMarkerColor(2)
hist2.Draw("same")

g.SetLineWidth(3)
g.Draw("same")

c1.SaveAs("pi.png")

