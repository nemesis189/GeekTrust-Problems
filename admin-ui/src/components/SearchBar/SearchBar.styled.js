import styled from "styled-components";

export const Wrapper = styled.div`
	display: flex;
	align-items: center;
	width: 100%;
	/* padding: 0 20px; */

	.searchBar-input-field {
		display: flex !important;
		align-items: center;
		padding: 0 10px;
	}
`;

export const Content = styled.div`
	position: sticky;
	background-color: rgba(245, 245, 245, 1) !important;
	width: 100%;

	input {
		color: black;
		background-color: rgba(245, 245, 245, 1) !important;
		padding: 10px;
		height: 35px;
		border: 0px;
		width: 700px;

		:focus {
			outline: none;
			border: none;
		}

		
	}

`;