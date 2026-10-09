"""
csv_profile.py - Simple CSV profiling script.
Prints count, missing, unique, and basic numeric stats per column.
"""

import csv, sys, statistics, collections

def profile_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        rdr = csv.DictReader(f)
        cols = rdr.fieldnames
        stats = {c: {'rows': 0, 'missing': 0, 'values': []} for c in cols}
        for row in rdr:
            for c in cols:
                val = row[c].strip()
                stats[c]['rows'] += 1
                if not val:
                    stats[c]['missing'] += 1
                else:
                    stats[c]['values'].append(val)
        for c in cols:
            values = stats[c]['values']
            print(f"\nColumn: {c}")
            print(f"  Rows: {stats[c]['rows']}")
            print(f"  Missing: {stats[c]['missing']}")
            print(f"  Unique: {len(set(values))}")
            nums = [float(v) for v in values if _is_float(v)]
            if nums:
                print(f"  Min: {min(nums):.3g}")
                print(f"  Max: {max(nums):.3g}")
                print(f"  Mean: {statistics.mean(nums):.3g}")
            else:
                counter = collections.Counter(values)
                if counter:
                    most_common = counter.most_common(1)[0]
                    print(f"  Most common: {most_common[0]} ({most_common[1]} times)")

def _is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python csv_profile.py <csv_file>")
        sys.exit(1)
    profile_csv(sys.argv[1])