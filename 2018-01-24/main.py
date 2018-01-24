import pencil


def create01():
    p = pencil.Pencil(3)
    return p

def totalRemainingLead(p):
    t = p.getNumLeads() * pencil.MAX_LEAD_LENGTH
    t += p.getCurrentLeadLength()
    return t

p1 = create01()
p1.addLeads(5)
for i in range(15):
    p1.click()
print(totalRemainingLead(p1))





