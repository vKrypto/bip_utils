# Copyright (c) 2021 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Imports
from tests.ecc.test_ecc import *


# Invalid keys for ed25519 coin addresses
TEST_ED25519_ADDR_INVALID_KEY_TYPES = (TEST_ED25519_BLAKE2B_PUB_KEY,
                                       TEST_NIST256P1_PUB_KEY,
                                       TEST_SECP256K1_PUB_KEY
                                       )
# Invalid keys for ed25519-blake2b coin addresses
TEST_ED25519_BLAKE2B_ADDR_INVALID_KEY_TYPES = (TEST_ED25519_PUB_KEY,
                                               TEST_ED25519_KHOLAW_PUB_KEY,
                                               TEST_ED25519_MONERO_PUB_KEY,
                                               TEST_NIST256P1_PUB_KEY,
                                               TEST_SECP256K1_PUB_KEY)
# Invalid keys for ed25519-monero coin addresses
TEST_ED25519_MONERO_ADDR_INVALID_KEY_TYPES = (TEST_ED25519_PUB_KEY,
                                              TEST_ED25519_BLAKE2B_PUB_KEY,
                                              TEST_ED25519_KHOLAW_PUB_KEY,
                                              TEST_NIST256P1_PUB_KEY,
                                              TEST_SECP256K1_PUB_KEY)
# Invalid keys for nist256p1 coin addresses
TEST_NIST256P1_ADDR_INVALID_KEY_TYPES = (TEST_ED25519_PUB_KEY,
                                         TEST_ED25519_BLAKE2B_PUB_KEY,
                                         TEST_ED25519_KHOLAW_PUB_KEY,
                                         TEST_ED25519_MONERO_PUB_KEY,
                                         TEST_SECP256K1_PUB_KEY)
# Invalid keys for secp256k1 coin addresses
TEST_SECP256K1_ADDR_INVALID_KEY_TYPES = (TEST_ED25519_PUB_KEY,
                                         TEST_ED25519_BLAKE2B_PUB_KEY,
                                         TEST_ED25519_KHOLAW_PUB_KEY,
                                         TEST_ED25519_MONERO_PUB_KEY,
                                         TEST_NIST256P1_PUB_KEY)
# Invalid keys for sr25519 coin addresses
TEST_SR25519_ADDR_INVALID_KEY_TYPES = (TEST_ED25519_PUB_KEY,
                                       TEST_ED25519_BLAKE2B_PUB_KEY,
                                       TEST_ED25519_KHOLAW_PUB_KEY,
                                       TEST_ED25519_MONERO_PUB_KEY,
                                       TEST_NIST256P1_PUB_KEY,
                                       TEST_SECP256K1_PUB_KEY)
