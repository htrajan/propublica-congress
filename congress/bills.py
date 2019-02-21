from .client import Client
from .utils import CURRENT_CONGRESS, check_chamber, get_offset


class BillsClient(Client):

    def by_member(self, member_id, type='introduced'):
        """
        Takes a bioguide ID and a type:
        (introduced|updated|cosponsored|withdrawn)
        Returns recent bills
        """
        path = "members/{member_id}/bills/{type}.json".format(
            member_id=member_id, type=type)
        return self.fetch(path)

    def get(self, bill_id, congress=CURRENT_CONGRESS, type=None):
        if type:
            path = "{congress}/bills/{bill_id}/{type}.json".format(
                congress=congress, bill_id=bill_id, type=type)
        else:
            path = "{congress}/bills/{bill_id}.json".format(
                congress=congress, bill_id=bill_id)

        return self.fetch(path)

    def amendments(self, bill_id, congress=CURRENT_CONGRESS):
        return self.get(bill_id, congress, 'amendments')

    def related(self, bill_id, congress=CURRENT_CONGRESS):
        return self.get(bill_id, congress, 'related')

    def subjects(self, bill_id, congress=CURRENT_CONGRESS):
        return self.get(bill_id, congress, 'subjects')

    def cosponsors(self, bill_id, congress=CURRENT_CONGRESS):
        return self.get(bill_id, congress, 'cosponsors')

    def recent(self, chamber, page=1, congress=CURRENT_CONGRESS, type='introduced'):
        """
        Takes a chamber, Congress, and type:
        (introduced|updated)
        Returns a list of recent bills
        """
        check_chamber(chamber)
        offset = get_offset(page)
        path = "{congress}/{chamber}/bills/{type}.json?offset={offset}".format(
            congress=congress, chamber=chamber, type=type, offset=offset)
        return self.fetch(path)

    def introduced(self, chamber, page=1, congress=CURRENT_CONGRESS):
        """Shortcut for getting introduced bills"""
        return self.recent(chamber, page, congress, 'introduced')

    def updated(self, chamber, page=1, congress=CURRENT_CONGRESS):
        """Shortcut for getting updated bills"""
        return self.recent(chamber, page, congress, 'updated')

    def passed(self, chamber, page=1, congress=CURRENT_CONGRESS):
        """Shortcut for passed bills"""
        return self.recent(chamber, page, congress, 'passed')

    def enacted(self, chamber, page=1, congress=CURRENT_CONGRESS):
        """Shortcut for enacted bills"""
        return self.recent(chamber, page, congress, 'enacted')

    def vetoed(self, chamber, page=1, congress=CURRENT_CONGRESS):
        """Shortcut for vetoed bills"""
        return self.recent(chamber, page, congress, 'vetoed')

    def upcoming(self, chamber, congress=CURRENT_CONGRESS):
        """Shortcut for upcoming bills"""
        path = "bills/upcoming/{chamber}.json".format(chamber=chamber)
        return self.fetch(path)
