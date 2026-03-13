# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42nice.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/13 13:13:38 by klucchin        #+#    #+#               #
#  Updated: 2026/03/13 13:47:45 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

entries_list = [
    "[ENTRY 000] New quantum  algorithm discovered",
    "[ENTRY 001] Efficiency increased by 374%",
    "[ENTRY 002] Archived by Data Archivist trainee"
]

name = "new_discovery.txt"
try:
    file = open(name, "w")
    print(f"Initializing new storage unit: {name}")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    for entry in entries_list:
        file.write(f"{entry}\n")
        print(f"{entry}")
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive {name} ready for long-term preservation")
    file.close()
except (FileNotFoundError, PermissionError):
    print("ERROR: couldnt find or write on long-term stone...")