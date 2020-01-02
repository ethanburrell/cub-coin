mod block_structure_poc;

fn generate_genesis_block() -> Box<block_structure_poc::Block> {
    let gs = Box::new(block_structure_poc::BlockStruct {
        index: 0,
        difficulty: 0,
        iv: 0,
        prev_hash: 0,
        timestamp: 0,
        data: 1234
    });

    let hash_data = Box::new([0; 256]);
    let mut genesis = Box::new(block_structure_poc::Block {
        block_struct: gs,
        hash: hash_data
    });
    block_structure_poc::create_block_hash(&mut genesis);
    return gs
}

#[cfg(test)]
mod tests {
    // Note this useful idiom: importing names from outer (for mod tests) scope.
    use super::*;

    #[test]
    fn test_validate_difficulty_0() {
        let genesis = generate_genesis_block();
        // We know the hash of this is:
        // [55, 74, 237, 229, 227, 198, 211, 59, 220, 113, 22, 60, 122,
        // 222, 147, 199, 46, 114, 232, 4, 221, 240, 104, 155, 232, 120,
        // 41, 49, 137, 76, 243, 189]
        // there are 2 leading zeros

        // test to see if there is one leading 0
        let ans = block_structure_poc::validate_difficulty(*genesis.hash, 0);
        assert_eq!(ans, false);
    }

    #[test]
    fn test_validate_difficulty_1() {
        let genesis = generate_genesis_block();
        let ans = block_structure_poc::validate_difficulty(*genesis.hash, 1);
        assert_eq!(ans, false);
    }
    #[test]
    fn test_validate_difficulty_2() {
        let genesis = generate_genesis_block();
        let ans = block_structure_poc::validate_difficulty(*genesis.hash, 2);
        assert_eq!(ans, true);
    }
    #[test]
    fn test_validate_difficulty_3() {
        let genesis = generate_genesis_block();
        let ans = block_structure_poc::validate_difficulty(*genesis.hash, 3);
        assert_eq!(ans, false);
    }
    #[test]
    fn test_validate_difficulty_4() {
        let genesis = generate_genesis_block();
        let ans = block_structure_poc::validate_difficulty(*genesis.hash, 4);
        assert_eq!(ans, false);
    }
    #[test]
    fn test_validate_difficulty_256() {
        let genesis = generate_genesis_block();
        let ans = block_structure_poc::validate_difficulty(*genesis.hash, 256);
        assert_eq!(ans, false);
    }
    #[test]
    #[should_panic]
    fn test_validate_difficulty_257() {
        let genesis = generate_genesis_block();
        let ans = block_structure_poc::validate_difficulty(*genesis.hash, 257);
        assert_eq!(ans, false);
    }
}
