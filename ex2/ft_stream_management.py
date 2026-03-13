# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_stream_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42nice.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/13 13:48:20 by klucchin        #+#    #+#               #
#  Updated: 2026/03/13 18:41:59 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

print("Input Stream active. Enter archivist ID: ")
archivist = input()

print("Input Stream active. Enter status report: ")
status = input()

sys.stdout.write(f"[STANDARD] Archive status from {archivist}: {status}\n")
sys.stderr.write("[ALERT] System diagnostic: communication channels verified\n")
sys.stdout.write("[STANDARD] Data transmission complete\n")

print("Three-channel communication test successeful")
