import React,{useEffect} from 'react';
import {useSelector,useDispatch} from 'react-redux';
import ProductComponent from './productComponent';
import axios from 'axios';
import {setProducts} from "../redux/actions/productActions";

const ProductListing = () => {
    const dispatch = useDispatch();
    const products = useSelector(state => state.allProducts);
    // console.log(products);
    const fetchProdcuts = async () => {
        const resp = await axios.get('https://fakestoreapi.com/products')
        .catch((err) => {
            console.log(err);
        })
        dispatch(setProducts(resp.data));
    }
    useEffect(() => {
        fetchProdcuts();
    }, []);
    return(
        <div className="ui grid container">
            <ProductComponent/>
        </div>
    )
}

export default ProductListing;