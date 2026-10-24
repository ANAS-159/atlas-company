# Decision note - architecture of the Atlas Industrie campus

## 1. Context and requirements

Atlas Industrie operates two buildings: Building A, containing the
head office and IT functions, and Building B, containing production.
The network must provide segmentation, controlled inter-zone traffic,
and resilience when Building A is isolated.

## 2. Technical targets retained

The design includes two core switches, two firewalls, and ten
access switches. VLANs separate infrastructure management, IT,
voice, guests, operational technology (OT), and the DMZ.

The addressing plan must include IPv4 and IPv6, avoid overlapping
subnets, and reserve VLAN 99 for unused ports without routed
addresses. Traffic between IT and OT follows a default-deny policy,
with only explicitly authorized flows permitted.

## 3. The two architectures compared

S1 is a three-tier architecture with two modular cores, four
distribution switches, ten access switches, and two firewalls.

S2 is a distributed collapsed-core architecture with two fixed
Layer 3 core switches in separate buildings, ten access switches,
and two firewalls.

S3 is a single-site collapsed-core architecture with both fixed
core switches in Building A, ten access switches, and two firewalls.

S3 is less expensive but does not satisfy the requirement that
production continue if Building A is isolated.

## 4. Five-year costing

All costs are in MAD, excluding tax, using the estimates supplied
by the lab. Annual support is 10% of CAPEX. Annual operations are
1.5 days per device at 5,400 MAD per day.

| Scenario | CAPEX | Five-year support | Five-year operations | Five-year TCO |
|---|---:|---:|---:|---:|
| S1 | 1,155,600 | 577,800 | 729,000 | 2,462,400 |
| S2 | 766,800 | 383,400 | 567,000 | 1,717,200 |
| S3 | 745,200 | 372,600 | 567,000 | 1,684,800 |

S2 saves 745,200 MAD compared with S1 over five years.
S2 costs 32,400 MAD more than S3 over five years.

At an assumed production outage cost of 108,000 MAD per hour,
the 32,400 MAD difference is equivalent to 18 minutes of downtime.

## 5. Decision and justification

S2 is recommended because it places the two core switches in
separate buildings while avoiding the additional distribution
layer and cost of S1.

S3 is cheaper, but it does not meet the stated resilience
requirement because both core switches are located in Building A.
The 32,400 MAD five-year premium of S2 is equivalent to 18 minutes
of production downtime at the assumed outage cost.

This financial comparison supports the decision but does not
guarantee service availability. The design must also be reviewed
for link failures, failover behavior, firewall dependencies,
power failures, and common physical failure points.

## 6. Risks and points of failure

The access switches remain potential single points of failure
for the devices connected to them. The physical fiber routes may
share a cable chamber or other common infrastructure, allowing
one incident to interrupt both links.

Separate core locations do not by themselves guarantee
resilience. Power, cooling, routing convergence, firewall
failover, and the actual physical paths must be verified.

The plan must not claim 99.99% availability without a complete
end-to-end reliability analysis.

## 7. Assumptions and limits

Equipment prices are estimates supplied by the lab, not vendor
quotations. Costs exclude power, cooling, civil works, and other
unpriced items. The exchange rate used by the lab is 1 EUR =
10.8 MAD.

The physical cable routes and UPS arrangements are assumptions
until verified against actual site documentation. The assumed
outage cost is 108,000 MAD per hour.

The cost comparison uses the lab's five-year support and
operations formulas. Availability, detailed failure probabilities,
and the performance of failover mechanisms require further study.
