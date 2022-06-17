import React, { useState, useEffect, useRef } from 'react';
import SearchIcon from '@mui/icons-material/Search';

import { Wrapper, Content } from './SearchBar.styled.js';

export default function SearchBar({ setSearchTerm }) {
    const [state, setState] = useState('');
    const initial = useRef(true);

    useEffect(() => {
        if (initial.current) {
            initial.current = false;
            return;
        }

            setSearchTerm(state);

        // return () => clearTimeout(timer);
    }, [setSearchTerm, state])


    return (
        <Wrapper>
            <Content>
                <div className="searchBar-input-field">
                    <SearchIcon className='search-icon' />
                    <input
                        id="searchBar"
                        type='text'
                        placeholder='Search Movie'
                        onChange={event => setState(event.currentTarget.value)}
                        value={state}
                        autoComplete="off"
                    />
                </div>
            </Content>
        </Wrapper>
    );
};
