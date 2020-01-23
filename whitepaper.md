# Proof of Rhythm (01/13/2020)
### Ethan Burrell
#### A work in progress design

------

Proof of Rhythm is a blockchain consensus algorithm under development for the
purpose of leader selection in a network of untrusted nodes. It builds on two
powerful examples of "leader election", the Proof of Work (PoW) model presented in Bitcoin's
white paper and Proof of Elapsed Time, a lesser known mechanism proposed by Intel.

PoW as presented in Bitcoin was extremely powerful at the time, it allowed new and easily
validated blocks to be added to a decentralized ledger. However, the process which elected these
blocks was extremely wasteful in terms of resources. As time progressed and the difficulty to discovering
new blocks increased, mining Bitcoin needed a large investment and expensive GPU or ASIC based
machines as well as wasteful power consumption.

Proof of Elapsed Time (PoET) solves the same problem as PoW, but
in a much smarter way. Instead of having a complicated hash-puzzle for miners to solve,
it uses Intel CPU's special instructions to prove that a node was the first one to awake
from sleep, electing a new leader to propose new blocks. This is better than generic PoW
in two ways: it greatly reduces the power consumption of a miner, and reduces the price
for a new miner to join the pool and effectively mine. However, there is a downside to
PoET, it requires specialized hardware for a miner to enter. Although the hardware is becoming
more common on consumer and enterprise motherboards, it still is [difficult to set up](https://software.intel.com/en-us/forums/intel-software-guard-extensions-intel-sgx/topic/671285). There is also security implications
of having a trusted enclave sign messages. In late 2019, [there were many security vulnerabilities](https://www.zdnet.com/article/manual-code-review-finds-35-vulnerabilities-in-8-enclave-sdks/)
found in Intel's SGX instructions, which allows this secure sandbox for running code to be
compromised by a malicious user. If PoET ran correctly, it could get around the difficult
voting inefficiencies that make Proof of Stake slow, and stop the power waste caused by
many other PoW algorithms. A Hyperledger Sawtooth, a system using PoET can handle 1300
transactions per second.


Proof of Rhythm is a proposed consensus algorithm that builds on the idea behind
Proof of Elapsed Time, while overcoming the hardware limitations of PoET. Proof of Rhythm
is another way to create a random time waiting algorithm that is verifiable by the block chain.
In PoET this is done by a signing key in the sandboxed SGX enclave. This allows for simple
cryptographic function calls to verify if the miner waited the correct amount of time.
A sidebar from the author, the idea behind verification here comes from signal processing, and initially
was conceptualized without the knowledge of PoET.

Proof of Rhythm uses a sinusoidal function to create long periods of the process being asleep,
with small moments of the process becoming awake. There are several tradeoffs here, and some
cryptonomics[correct word for this] in play. There are some guarantees that this process must give:
1. The elected node must have waited according to its function, in a way that is verifiable
by the network.
2. The winning node must be selected at random, so nodes running functions with different
periods have the same probability of becoming selected. (Working on a proof for this currently)

Both of these points must be ensured to have this be a secure way to discover new blocks.
If (1) is violated, then malicious actors can fake their waiting times and always win the race.
(2) If an honest user can more frequently win the election process by using a function with
shorter period than a node using a longer period, this will create large imbalances in
election and could favor malicious users.
