"""Tests for the region enum"""
from typing import List
import numpy as np
from life_expectancy.regions import Region

def test_regions_list(regions_expected: List[str]):
    """Test for the region listing function"""

    region_list = Region.list_countries()
    np.testing.assert_array_equal(region_list, regions_expected)