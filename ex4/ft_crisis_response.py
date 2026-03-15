# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_crisis_response.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/15 16:04:40 by klucchin        #+#    #+#               #
#  Updated: 2026/03/15 16:45:30 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

try:
    print("CRISIS ALERT: Attempting acceess to 'lost_archive.txt'...")
    with open("lost_archive.txt") as lost_file:
        file = lost_file.read()
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
finally:
    print("STATUS: Crisis handled, system stable\n")

try:
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    with open("classified_data.txt") as classified_data:
        data = classified_data.read()
except (FileNotFoundError, PermissionError):
    print("RESPONSE: Security protocol deny access")
finally:
    print("STATUS: Crisis handled, security maintained\n")

try:
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    with open("standard_archive.txt") as standard_file:
        standard = standard_file.read()
        print(f"SUCCESS: Archive recovered - : ''{standard}''")
except (FileNotFoundError, PermissionError):
    print("ERROR: not suposed to happen\n")
finally:
    print("STATUS: Normal operations resumed\n")

print("All crisis scenarios handled successfully. Archives secure.")