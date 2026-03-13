# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42nice.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/13 12:30:11 by klucchin        #+#    #+#               #
#  Updated: 2026/03/13 13:12:17 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

name = "ancient_fragment"
try:
    file = open("ancient_fragment.txt")
    print(f"Accessing Storage Vault: {name}")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    print(f"{file.read()}\n")
    print("Data recovery complete. Storage unit disconnected.")
    file.close()
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
