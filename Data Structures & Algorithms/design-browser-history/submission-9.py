class ListNode:
    # One node = one page in the browser history.
    # It remembers the page's url, plus the page before (prev) and after (next) it.
    def __init__(self, val, prev=None, next=None):
        self.val = val      # the url of this page
        self.prev = prev    # link to the previous page (back direction)
        self.next = next    # link to the next page (forward direction)


class BrowserHistory:

    def __init__(self, homepage: str):
        # Start with just the homepage. cur = the page we're on right now.
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        # Make a new node for the new page, linked back to the current page
        self.cur.next = ListNode(url, self.cur)
        # Move to the new page.
        # Overwriting cur.next also throws away any old "forward" history
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        # Go back one page at a time, until we run out of steps
        # or hit the first page (no prev left)
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        # Return the url of the page we ended up on
        return self.cur.val

    def forward(self, steps: int) -> str:
        # Same idea, but moving toward newer pages
        # Stops at the last page (no next left)
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)