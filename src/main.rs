mod block_structure_poc;
fn main() {
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

    println!("the hash, in main= {:?}", &genesis.hash[31 .. 64]);

    //println!("{}", genesis.hash);

    let ans = block_structure_poc::validate_difficulty(*genesis.hash, 0);
    println!("should be false = {}", ans);
    let ans = block_structure_poc::validate_difficulty(*genesis.hash, 1);
    println!("should be false = {}", ans);
    let ans = block_structure_poc::validate_difficulty(*genesis.hash, 2);
    println!("should be true = {}", ans);

    let ans = block_structure_poc::validate_difficulty(*genesis.hash, 33);
    println!("should be false = {}", ans);

}
