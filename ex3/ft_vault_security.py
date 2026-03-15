# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_vault_security.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/15 15:46:02 by klucchin        #+#    #+#               #
#  Updated: 2026/03/15 16:06:40 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

print("Initiating secure vault access...")

try:
    print("Vault connection established with failsafe protocols\n")

    with open("classified_data.txt", "r") as vault_file:
        data = vault_file.read()
        print("SECURE EXTRACTION:")
        print(f"{data}\n")

    with open("classified_vault.txt", "w") as archive_file:
        archive_file.write("[CLASSIFIED] New security protocols archived")
        print("SECURE PRESERVATION:")
        print("[CLASSIFIED] New security protocols archived")

    print("Vault automatically sealed upon completion\n")
except (FileNotFoundError, PermissionError):
    print("Error: Vault source not found/Permission denied")
finally:
    print("All vault operations completed with maximum security.")
