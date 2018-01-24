MAX_LEAD_LENGTH = 10
MAX_NUM_LEADS = 5


class Pencil:
    def __init__(self, num_leads):
        self.mNumLeads = 0
        self.mCurrentLeadLength = MAX_LEAD_LENGTH
        self.addLeads(num_leads)
        return

    def getNumLeads(self):
        return self.mNumLeads

    def getCurrentLeadLength(self):
        return self.mCurrentLeadLength

    def click(self):
        if self.mCurrentLeadLength > 0:
            self.mCurrentLeadLength -= 1
        if self.mCurrentLeadLength == 0 and self.mNumLeads > 0:
            self.mCurrentLeadLength = MAX_LEAD_LENGTH
            self.mNumLeads -= 1
        return self.mCurrentLeadLength > 0

    def addLeads(self, num_additional_leads):
        if num_additional_leads > 0:
            self.mNumLeads += num_additional_leads
            if self.mNumLeads > MAX_NUM_LEADS:
                self.mNumLeads = MAX_NUM_LEADS
