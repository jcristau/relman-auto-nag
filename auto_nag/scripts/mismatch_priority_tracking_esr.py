# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from auto_nag import utils
from auto_nag.bzcleaner import BzCleaner


class MismatchPrioTrackESR(BzCleaner):
    def __init__(self):
        super(MismatchPrioTrackESR, self).__init__()
        self.init_versions()

    def description(self):
        return "Bug tracked for esr with a bad priority (P3, P4 or P5)"

    def template(self):
        return "mismatch_priority_tracking.html"

    def ignore_date(self):
        return True

    def get_bz_params(self, date):
        esr_version = self.versions["esr"]
        value = ",".join(["---", "affected"])
        params = {
            "resolution": [
                "---",
                "FIXED",
                "INVALID",
                "WONTFIX",
                "DUPLICATE",
                "WORKSFORME",
                "INCOMPLETE",
                "SUPPORT",
                "EXPIRED",
                "MOVED",
            ],
            "priority": ["P3", "P4", "P5"],
            "f1": utils.get_flag(esr_version, "tracking", "esr"),
            "o1": "anyexact",
            "v1": ",".join(["+", "blocking"]),
            "f2": utils.get_flag(esr_version, "status", "esr"),
            "o2": "anyexact",
            "v2": value,
        }
        return params

    def get_autofix_change(self):
        return {
            "comment": {
                "body": "Changing the priority to p1 as the bug is tracked by a release manager for the current esr.\nSee [What Do You Triage](https://firefox-source-docs.mozilla.org/bug-mgmt/guides/priority.html) for more information"
            },
            "priority": "p1",
        }


if __name__ == "__main__":
    MismatchPrioTrackESR().run()
