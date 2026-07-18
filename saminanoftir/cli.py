"""CLI for peak finding."""
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Find peaks in spectroscopy data")
    parser.add_argument("file", help="Input CSV or TXT file")
    parser.add_argument("--method", default="ftir", choices=["ftir", "raman", "xrd"])
    args = parser.parse_args()
    print(f"[saminanoftir] Finding {args.method} peaks in {args.file} (demo)")
    print("Peak detection complete. (Extend with real scipy.signal.find_peaks logic)")
    sys.exit(0)

if __name__ == "__main__":
    main()