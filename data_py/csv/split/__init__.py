"""
Data Splitter Package

A Python library for splitting datasets into training, testing, and validation sets.
Supports various splitting strategies such as basic split, stratified split, time series split, and more.

Functions:
- data_split: Basic data splitting.
- data_split_stratified: Stratified sampling based on a target column.
- data_split_time_series: Time-based splitting.
- data_split_by_condition: Split data based on a condition.
- data_split_custom_ratio: Split data with custom ratios.
- data_split_by_distribution: Split data while preserving the distribution of a target column.
- data_split_by_group: Split data based on groups.
- data_split_cross_validation: Generate cross-validation folds.
"""

# Core splitting functions
from .data_split import data_split
from .data_split_stratified import data_split_stratified
from .data_split_time_series import data_split_time_series

# Advanced splitting functions
from .data_split_by_condition import data_split_by_condition
from .data_split_custom_ratio import data_split_custom_ratio
from .data_split_by_distribution import data_split_by_distribution
from .data_split_by_group import data_split_by_group

# Cross-validation
from .data_split_cross_validation import data_split_cross_validation


__all__ = [
    'data_split',
    'data_split_stratified',
    'data_split_time_series',
    'data_split_by_condition',
    'data_split_custom_ratio',
    'data_split_by_distribution',
    'data_split_by_group',
    'data_split_cross_validation',
]