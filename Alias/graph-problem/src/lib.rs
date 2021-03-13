// internal imports
use std::collections::{HashMap, HashSet, hash_map::Keys};
use std::hash::Hash;

//external imports
use uuid::Uuid;
use rand;

#[derive(Debug)]
pub struct HashGraph<T: Eq + Hash> {
    graph: HashMap<T, Vec<T>>,
}

#[allow(dead_code)] // remove later
impl<T: Eq + Hash> HashGraph<T> {
    fn new_empty() -> Self {
        Self {
            graph: HashMap::new(),
        }
    }

    fn with_capacity(capacity: usize) -> Self {
        Self {
            graph: HashMap::with_capacity(capacity),
        }
    }

    fn new_from(graph: HashMap<T, Vec<T>>) -> Self {
        Self {
            graph: graph,
        }
    }

    fn len(&self) -> usize {
        self.graph.len()
    }

    fn keys<'a>(&'a self) -> Keys<'a, T, Vec<T>> {
        self.graph.keys()
    }


    fn insert(&mut self, k: T, v: Vec<T>) -> Option<Vec<T>> {
        self.graph.insert(k, v)
    }

    fn gen_rand_uuid(num_v: usize) -> Self {
        let mut out: Self = HashGraph::with_capacity(num_v);
        let mut vertices: Vec<Uuid> = Vec::with_capacity(num_v);

        for _ in 0..num_v {
            vertices.push(Uuid::new_v4());
        }

        for vertex in vertices {
            

            // out.insert()
        }

        out
    }
}
