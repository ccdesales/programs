"""
Test set for distance_among_points
"""
import nose
from nose.tools import eq_, ok_
from data_structures.basics.distance_among_points import DistanceCalculator

def test_are_same_sign():
    dc = DistanceCalculator()
    eq_(dc.are_same_sign(0, 0), True)
    eq_(dc.are_same_sign(0, 1), True)
    eq_(dc.are_same_sign(1, 0), True)
    eq_(dc.are_same_sign(0, -1), False)
    eq_(dc.are_same_sign(-1, 0), False)

def test_manhatan_distance_from_origin_plus():
    dc = DistanceCalculator()
    eq_( dc.manhatan_distance(
            (0, 0),
            (0, 4)
        ), 4
    )
        
    eq_( dc.manhatan_distance(
            (0, 0),
            (5, 0)
        ), 5
    )
    
    eq_( dc.manhatan_distance(
            (0, 0),
            (2, 4)
        ), 6
    )
    
    eq_( dc.manhatan_distance(
            (0, 0),
            (7, 3)
        ), 10
    )
    
def test_manhatan_distance_from_origin_all_negative():
    dc = DistanceCalculator()
    eq_( dc.manhatan_distance(
            (0, 0),
            (0, -4)
        ), 4
    )
        
    eq_( dc.manhatan_distance(
            (0, 0),
            (-5, 0)
        ), 5
    )
    
    eq_( dc.manhatan_distance(
            (0, 0),
            (-2, -4)
        ), 6
    )
    
    eq_( dc.manhatan_distance(
            (0, 0),
            (-7, -3)
        ), 10
    )

def test_manhatan_distance_from_origin_minus():
    dc = DistanceCalculator()
    
    eq_( dc.manhatan_distance(
            (0, 0),
            (2, -4)
        ), 6
    )
        
    eq_( dc.manhatan_distance(
            (0, 0),
            (-5, 10)
        ), 15
    )
    
def test_manhatan_distance():
    dc = DistanceCalculator()
    eq_( dc.manhatan_distance(
            (1, 2),
            (-1, -2)
        ), 6
    )
        
    eq_( dc.manhatan_distance(
            (1, 2),
            (-2, 3)
        ), 4
    )
    
    eq_( dc.manhatan_distance(
            (3, -5),
            (-2, -1)
        ), 9
    )
    
    eq_( dc.manhatan_distance(
            (1, -2),
            (2, 3)
        ), 6
    )
    
def test_minimal_distance():
    dc = DistanceCalculator()
    points = (
        (-2, -2),
        (1, 2),
        (-1, 7),
        (4, -2),
    )
    eq_( dc.is_minimal_distance(points, minimal_distance=5), True )

def test_no_minimal_distance():
    dc = DistanceCalculator()
    points = (
        (1, 0),
        (1, 2),
        (-1, 3),
        (4, -2),
    )
    eq_( dc.is_minimal_distance(points, minimal_distance=5), False )
    
    points = (
        (-2, -2),
        (3, 1),
        (-1, 3),
        (4, -2),
    )
    eq_( dc.is_minimal_distance(points, minimal_distance=5), False )


    points = (
        (-2, -2),
        (1, 0),
        (-1, 3),
        (3, -2),
    )
    eq_( dc.is_minimal_distance(points, minimal_distance=5), False )


def run():
    nose.run()
    
if __name__ == '__main__':
    run()