import os


def insert_after_front_matter(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if lines[0].strip() != "---":
        print("No front matter found.")
        return

    # Find the end of the front matter
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            front_matter_end_index = i
            break
    else:
        print("Front matter end not found.")
        return

    # Insert the line after the front matter
    lines.insert(
        front_matter_end_index + 1, "\nFrom: [[dwarkesh | The Dwarkesh Podcast]]\n\n"
    )

    # Write the updated content back to the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print("Inserted line after front matter.")


if __name__ == "__main__":
    directory = "dwarkesh_podcast"
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            file_path = os.path.join(directory, filename)
            insert_after_front_matter(file_path)
