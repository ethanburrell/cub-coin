mod tests;
mod block_structure;
use std::env;

use tokio::net::TcpListener;
use tokio::prelude::*;
use futures::stream::StreamExt;
#[tokio::main]
async fn main() {
    let addr = "127.0.0.1:6142";
    let mut listener = TcpListener::bind(addr).await.unwrap();

    // Here we convert the `TcpListener` to a stream of incoming connections
    // with the `incoming` method. We then define how to process each element in
    // the stream with the `for_each` combinator method
    let server = async move {
        let mut incoming = listener.incoming();
        while let Some(socket_res) = incoming.next().await {
            match socket_res {
                Ok(socket) => {
                    println!("Accepted connection from {:?}", socket.peer_addr());
                    // TODO: Process socket
                }
                Err(err) => {
                    // Handle error by printing to STDOUT.
                    println!("accept error = {:?}", err);
                }
            }
        }
    };

    println!("Server running on localhost:6142");

    // Start the server and block this async fn until `server` spins down.
    server.await;
}
// fn main() {
//     let args: Vec<String> = env::args().collect();
//     if args[1] == "server" {
//
//     } else {
//
// }
// }

// use std::net::TcpListener;
// use std::thread::spawn;
// use tungstenite::server::accept;
//
//
// use tungstenite::handshake::client::{Request};
// use std::env;
//
// use tungstenite::{connect, Message};
// use url::Url;
//
// fn main() {
//     // A WebSocket echo server
//     let args: Vec<String> = env::args().collect();
//     println!("{:?}", args);
//     if args[1] == "server" {
//         println!("server");
//         let server = TcpListener::bind("127.0.0.1:9001").unwrap();
//         for stream in server.incoming() {
//             spawn (move || {
//                 let mut websocket = accept(stream.unwrap()).unwrap();
//                 loop {
//                     let msg = websocket.read_message().unwrap();
//
//                     // We do not want to send back ping/pong messages.
//                     if msg.is_binary() || msg.is_text() {
//                         websocket.write_message(msg).unwrap();
//                     }
//                 }
//             });
//         }
//     } else {
//         println!("client");
//         let (mut socket, response) =
//             connect(Url::parse("ws://localhost:3012/socket").unwrap()).expect("Can't connect");
//
//         println!("Connected to the server");
//         println!("Response HTTP code: {}", response.status());
//         println!("Response contains the following headers:");
//         for (ref header, _value) in response.headers() {
//             println!("* {}", header);
//         }
//
//         socket
//             .write_message(Message::Text("Hello WebSocket".into()))
//             .unwrap();
//         loop {
//             let msg = socket.read_message().expect("Error reading message");
//             println!("Received: {}", msg);
//         }
//         // socket.close(None);
//     }
//     // socket.close(None);
// }

/*
#![feature(proc_macro_hygiene, decl_macro)]

#[macro_use] extern crate rocket;

mod tests;
mod block_structure;

#[get("/hello/<name>/<age>")]
fn hello(name: String, age: u8) -> String {
    format!("Hello, {} year old named {}!", age, name)
}

fn main() {
    rocket::ignite().mount("/", routes![hello]).launch();
}
*/
