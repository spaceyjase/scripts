import unittest
import re

from rrbot_regex import what_regex


class TestRegex(unittest.TestCase):

    def test_match(self):
        self.assertTrue(re.search(what_regex,
                        'what is the rr?', re.IGNORECASE), "Should be True")

    def test_match_whats_the_rr(self):
        self.assertTrue(re.search(what_regex, 'whats the rr',
                        re.IGNORECASE), "Should be True")

    def test_regex_match_rr(self):
        query = 'rr?'
        self.assertTrue(re.search(what_regex, query,
                                 re.IGNORECASE), "Should be True")

    def test_regex_match_what_is_the_rr(self):
        query = "what is the rr?"
        self.assertTrue(re.search(what_regex, query,
                                 re.IGNORECASE), "Should be True")

    def test_regex_match_what_the_rr(self):
       query = "what the rr?"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_what_is_rr(self):
       query = "what is rr?"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_what_rr_qm(self):
       query = "what rr?"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_what_rr(self):
       query = "what rr"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_what_s_the_rr(self):
       query = "what's the rr?"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_what_s_the_rr_quoted(self):
       query = '"what''s the rr?"'
       self.assertFalse(re.search(what_regex, query,
                                 re.IGNORECASE), "Should be False")

    def test_regex_match_what_s_the_rr_quoted_text(self):
       query = 'Sarcasm, "What''s the rr?" folks snafu.'
       self.assertFalse(re.search(what_regex, query,
                                 re.IGNORECASE), "Should be False")

    def test_regex_match_what_s_the_rr_quoted_text_case(self):
       query = '"What''s the RR?"'
       self.assertFalse(re.search(what_regex, query,
                                 re.IGNORECASE), "Should be False")

    def test_regex_match_what_s_the_rr_quoted_text_no_match(self):
       query = 'When somebody asks, "What is the RR?".'
       self.assertFalse(re.search(what_regex, query,
                                 re.IGNORECASE), "Should be False")

    def test_regex_match_what_is_the_rr_and_match(self):
       query = "I'm new to this sub and I would like to ask for some help: What is the RR and where do I find it? ^"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_what_is_rr_with_text(self):
       query = "can someone tell me what is rr? have i missed something?"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_what_is_the_rr_with_text(self):
       query = 'can someone tell me what is the rr? have i missed something?'
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_also_what_is_the_rr(self):
       query = "Also, what is rr?"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_what_is_rr_match(self):
       query = "what is rr"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_wat_rr_match(self):
       query = "wat rr"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_what_is_rr_match_2(self):
       query = "what is rr."
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_rr_match(self):
       query = "RR?"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_quote_rr_quote_no_match(self):
       query = '"rr?"'
       self.assertFalse(re.search(what_regex, query,
                                 re.IGNORECASE), "Should be False")

    def test_regex_match_text_what_the_rr_no_match(self):
       query = "I tried to decipher what the RR was asking me to do in a workout..."
       self.assertFalse(re.search(what_regex, query,
                                 re.IGNORECASE), "Should be False")

    def test_regex_match_text_what_does_the_rr_match(self):
       query = "what does the rr?"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_text_what_is_the_rr_stand_for_match(self):
       query = "what is the rr stand for?"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_text_what_does_the_rr_stand_for_match(self):
       query = "what does the rr stand for?"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_text_what_does_the_rr_mean_match(self):
       query = "what does rr mean?"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_text_foo_define_rr_bar_match(self):
       query = "foo define rr bar"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_text_define_rr_match(self):
       query = "define rr?"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_text_define_rr_spacing_match(self):
       query = "define rr    ggsddg"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_text_no_match(self):
       query = "define nothing rr    ggsddg"
       self.assertFalse(re.search(what_regex, query,
                                 re.IGNORECASE), "Should be False")

    def test_regex_match_odd_quote_text_match(self):
       query = "what`s the rr?"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_odd_quote_text_no_match(self):
       query = '"what`s the rr?"'
       self.assertFalse(re.search(what_regex, query,
                                 re.IGNORECASE), "Should be False")

    def test_regex_match_unicode_from_test_sub(self):
       query = 'Yeah but what’s the RR? I should have a reply…'
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_unicode_from_test_sub_match(self):
       query = "Yeah but what's the RR? I should have a reply…"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_from_test_dumb(self):
       query = 'Sorry i may seem dumb but whats the rr'
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_from_test_whats_the_rr(self):
       query = "whats the Rr"
       self.assertTrue(re.search(what_regex, query,
                                re.IGNORECASE), "Should be True")

    def test_regex_match_quote_from_test_whats_the_rr_no_match(self):
       query = '"whats the Rr"'
       self.assertFalse(re.search(what_regex, query,
                                 re.IGNORECASE), "Should be False")


if __name__ == '__main__':
    unittest.main()
