from __future__ import absolute_import, unicode_literals

import datetime

import pytest

from tests.factories.page import ContentPageFactory
from tests.factories.rule import (
    DayRuleFactory, DeviceRuleFactory, ReferralRuleFactory, TimeRuleFactory)
from tests.factories.segment import SegmentFactory
from tests.factories.site import SiteFactory
from wagtail_personalisation.models import Segment
from wagtail_personalisation.rules import TimeRule

# Factory tests

@pytest.mark.django_db
def test_segment_create():
    factoried_segment = SegmentFactory()
    segment = Segment(name='TestSegment', enabled='enabled')
    TimeRule(
        start_time=datetime.time(8, 0, 0),
        end_time=datetime.time(23, 0, 0),
        segment=segment)

    assert factoried_segment.name == segment.name
    assert factoried_segment.enabled == segment.enabled




@pytest.mark.django_db
def test_referral_rule_create():
    segment = SegmentFactory(name='Referral')
    referral_rule = ReferralRuleFactory(
        regex_string='test.test',
        segment=segment)

    assert referral_rule.regex_string == 'test.test'
