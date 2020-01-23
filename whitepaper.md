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

Proof of Rhythm uses a sinusoidal series to create long periods of the process being asleep,
with small moments of the process becoming awake. There are several tradeoffs here, and some
cryptonomics[correct word for this] in play. There are some guarantees that this process must give:
1. The elected node must have waited according to its function, in a way that is verifiable
by the network.
2. The winning node must be selected at random, so nodes running functions with different
series have the same probability of becoming selected. (Working on a proof for this currently)

Both of these points must be ensured to have this be a secure way to discover new blocks.
If (1) is violated, then malicious actors can fake their waiting times and always win the race.
(2) If a user can consistently win the
The second is a way to encourage participation in the network. Unlike normal PoW, the overall cost
of setting up a mining system is extremely small, so there is not major incentive to send the new block to
one user.

#### Why build upon Proof of Elapsed Time

While PoET is only used by [Hyperledger Sawtooth](https://sawtooth.hyperledger.org/), There are reasons
that make a system like PoET perfect for selecting a leader uniformly at random from a population.
First, all PoW algorithms most general __ is to order elements proposed from a network of
untrusted individuals. PoR builds upon this, and creates a energy efficient way to do so.


#### Algorithm

Each node defines and *a* and *c*, so their pings are defined by the equation:

![cos\left(ax\right)+c](https://render.githubusercontent.com/render/math?math=cos%5Cleft(ax%5Cright)%2Bc)

This defines the amount of time to wait between "awake" moments. This is the underlying mechanism
to determine the winner, however in doing this it is very difficult to guarantee that a node is not
lying about when it awakes. Again, the first to awake is the block leader.

Keeping track of each nodes interval is important to the integrity of the system. If
nodes are able to maliciously change their waiting time intervals.

| Data sent by node |
| ------------- |
| serialized function  |
| signed function      |
| node's public signing key (PSK) |

This packet is sent to validator nodes. There are 2 approaches for these: one being totally
decentralized and one centralized.

###### A centralized approach

Similar to the hashgraph, we look at the median received time for the validators.

This process of checking to see that the packets roughly meet their period is easy to
determine on a small amount of trusted validators. The performance on this small validator
set, will be very good.

Downsides to this, it requires a centralized entity. However, this operates in an interesting way.
Generally, there is a trade off is made between between centralization and performance. A
centralized system generally performs better than a decentralized one, but with less privacy
for the users.


Revise \/

For this centralized approach, only the system keeping track of the beat of each client is
centralized while the distributed ledger is not centralized. The centralized validators can
only claim that a certain node was not on the correct rhythm. Even if the centralized system
was un-trusted the nodes would be able to see the #

# Node connecting to the network

When a node connects to the network there is a process in place to determine a users
network delay, after all for our validators to be able to determine if a user is spoofing
their period, it is a function of their waiting time and the delay in network.

Attack Vectors:

1. Adding extra delay, during this "training" period
2. Sending UDP packet early


There is many different attack vectors that could happen here that all have to
do with timing between a malicious node and the trusted centralized network. The
centralized network can run a common outlier detection algorithm to determine if an
individual node is spoofing, or if a network connection at a specific time is slow.

##### Reward and Penalty for "lying nodes"

The centralized validator nodes can't determine if an individual node is lying
(there is no benefit to claiming a node awakes late) or just has a unusually slow
connection on a single instance. Likewise, the validators can't distinguish a fast connection
from a lying node. There were several different ideas I had when creating this to
prevent a "early wake up" attack, such as:
1. Broadcast a message from a validator to all "miner" nodes, have the nodes hash this,
and send it back to the validators in the packet

However, this approach leaves room for inequality between miners who have fast and
slow connections, faster connection miners, would get a headstart on computing this
hash value. (See how hashgraph deals with this and POET)






since we do get better performance out

Even though this has a small




------

------

![e^{i\pi }=-1](https://render.githubusercontent.com/render/math?math=e%5E%7Bi%5Cpi%20%7D%3D-1)

https://alexanderrodin.com/github-latex-markdown/?math=e%5E%7Bi%5Cpi%20%7D%3D-1

https://www.youtube.com/watch?v=cpXkMZqtLl0
