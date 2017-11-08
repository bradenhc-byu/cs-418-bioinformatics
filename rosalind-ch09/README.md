# Personal Genomics
### Why?

Nicholas Volker was the first person to have his life saved by genome sequencing
(2010)
- Had a rare disease that was threatening his life
- His doctor was able to use genome sequencing to determine that the young boy
  needed a bone marrow transplant
- The boy's life was saved

Personal genomics can help us understand the genetic basis of diseases.

Some concerns people have:
- Genetic information can cause discrimination
- We are uniquely identifiable by our genetic mutations
- Some people don't want to know if they are going to die early

Common Variable Immune Difficiency (CVID)

### How can we assemble individual genomes efficiently using the reference?

***Why not use assembly?***
- Computationally expensive
- Genes that have mutated may not be able to be assembled
- We may not be concerned with the entire genome
- It's a different problem using a more difficult approach
    - We aren't taking advantage of the fact that we have a copy already
    
#### Read Mapping
Read mappings determine where each read has high similarity to the reference 
genome

***Multiple Pattern Matching Problem:***
Brute force works, it's easy, but it's too slow. One solution is to put all 
the sequences "on a bus" and traverse the reference all at once.

We can build a trie to help solve this problem