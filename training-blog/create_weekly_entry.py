import os

def create_weekly_entry(week_number):
  """
  Creates a new Markdown file for a weekly entry within the 'training-weeks' directory.
  """
  # Modify the filename format to directly create week-X.md files
  index_file = f"training-weeks/week-{week_number}.md"

  # Check if 'training-weeks' directory exists, create it if not
  if not os.path.exists("training-weeks"):
    os.makedirs("training-weeks")

  with open(index_file, "w") as f:
    f.write(f"# Week {week_number} Training\n\n")
    f.write("**Topics Covered:**\n\n")
    f.write("**Detailed Explanation:**\n\n")
    f.write(" (Write your detailed explanation here)\n\n")
    # Add more optional sections as needed

if __name__ == "__main__":
  week_number = int(input("Enter the week number: "))
  create_weekly_entry(week_number)
  print(f"Week {week_number} entry created successfully!")

