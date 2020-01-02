use serde::{Serialize, Deserialize};
use crypto::digest::Digest;
use crypto::sha2::Sha256;
//#[derive(Serialize, Deserialize, Debug)]


pub trait BlockTrait
{
    //fn generate_hash(&block_struct : BlockStruct);
    fn generate_hash(self);

}

#[derive(Serialize, Deserialize)]
pub struct BlockStruct {
    // A rectangle can be specified by where the top left and bottom right
    // corners are in space.
    pub index: u8,
    pub difficulty: u8,
    pub iv: u128,
    pub prev_hash: u128,
    pub timestamp: u32,
    pub data: u128
}

pub struct Block {
    pub block_struct: Box<BlockStruct>,
    //*mut BlockStruct,
    pub hash: Box<[u8; 256]>
    //[u8; 256]//[u8]
    //u128
    //GenericArray<u8, 256>,
}
/*
impl BlockTrait for Block {
    //fn generate_hash(block_struct : BlockStruct) {
    fn generate_hash(self) {
        //println!("{}", self.block_struct);
        println!("{}", "hello");
        //return ();//"{} the dog said: bork!";
        self.hash = 69;
    }
}*/
/*
let genesisStruct = BlockStruct {
    index: 0,
    difficulty: 0,
    iv: 0,
    prevHash: 0,
    timestamp: 0,
    data: "asdf"
}

let genesisBlock = Block{

}
*/



pub fn create_block_hash(block: &mut Box<Block>) {
    println!("changed hash!");
    println!("{}", block.block_struct.data);
    let unboxed_point = &*block.block_struct;
    let serialized = serde_json::to_string(&unboxed_point).unwrap();
    println!("serialized={}", serialized);
    let mut hasher = Sha256::new();
    hasher.input(serialized.as_bytes());

    //let output: &mut [u8; 256] = &mut [0b00000000u8; 256];
    let mut output: [u8; 256] = [0b00000000u8; 256];
    hasher.result(&mut output);
    println!("the hash, in setter function = {:?}", &output[0 .. 31]);
    // set hash to be the one we have
    block.hash = Box::new(output);
    //block.hash = result;
}


pub fn validate_difficulty(hash: [u8; 256], difficulty: u32) -> bool {
    if difficulty > 256 {
        //throw_new!("Difficulty is over 32");
        panic!("Difficulty is over 256");
    }

    let num_bytes: usize = ((difficulty / 8) + 1) as usize;
    let bits_leftover = difficulty % 8;
    println!("bits leftover {}, difficulty {}", bits_leftover, difficulty);
    // assert if num_bytes > 32

    for i in 0..num_bytes {
        println!("{}, leading 0s {}", i, hash[i].leading_zeros());
        if i == num_bytes - 1 {
            if hash[i].leading_zeros() != bits_leftover {
                return false
            }
        } else {
            if hash[i].leading_zeros() != 8 {
                return false
            }
        }
    }
    return true
}
