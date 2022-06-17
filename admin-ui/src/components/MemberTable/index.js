import React, { useState, useEffect } from "react";
import Checkbox from '@mui/material/Checkbox';
import Table from '@mui/material/Table';
import TableHead from '@mui/material/TableHead';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableFooter from '@mui/material/TableFooter';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import IconButton from '@mui/material/IconButton';

//Custom Component
import EditRowModal from '../EditRowModal';
import TablePaginationActions from '../CustomPaginationActions'
import SearchBar from '../SearchBar';


//API
import {getMembersData} from "../../API";

//style
import {IconWrapper, PaginationWrapper} from "./MemberTable.styled";
import DeleteIcon from '@mui/icons-material/Delete';
import ModeEditOutlineIcon from '@mui/icons-material/ModeEditOutline';



export default function MemberTable() {
	
	const [page, setPage] = useState(0);
	const [rows, setRows] = useState([]);
	const [rowsPerPage, setRowsPerPage] = useState(10);
	const rowsRef = React.createRef();
	rowsRef.current = rows;
	console.log("REFERENCE ROWS", rowsRef);
	const [selected, setSelected] = useState([]);
	const [editRow, setEditRow] = useState(false);
	const [modalOpen, setModalOpen] = useState(false);
	const [searchTerm, setSearchTerm] = useState('');
	const unfilteredRows = JSON.parse(sessionStorage.getItem('memberRows'));

	const columns = ['Id', 'Name', 'Email', 'Role', 'Actions']
	
	// Retrieving member data from API and setting it as rows if sessionStorage is empty
	const setRowsInMemoryAndState = (rows) => {
		sessionStorage.setItem('memberRows', JSON.stringify(rows));
		setRows(rows);
	};

	useEffect(() => {
		getMembersData((resp) => {
			let rowsInStorage = JSON.parse(sessionStorage.getItem('memberRows'));
			if (!rowsInStorage || !rowsInStorage.length) {
				if (resp.data) {
					setRowsInMemoryAndState(resp.data);
				} 
			} else {
				setRows(rowsInStorage);
			}
		});
	}, []);

// Filtering as per search keyword
	useEffect(() => {
		if(searchTerm) {
			const newFilter = unfilteredRows.filter(member => {
				return (
					member.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
					member.email.toLowerCase().includes(searchTerm.toLowerCase()) ||
					member.role.toLowerCase().includes(searchTerm.toLowerCase())
				);
			})
			setRows(newFilter)
		} else {
			setRows(unfilteredRows);
		}
	}, [searchTerm, setSearchTerm]);
	
	// Avoid a table shrink when reaching the last page with empty rows(fewer rows than rowsPerPage).
	const emptyRows = page > 0 ? Math.max(0, (1 + page) * rowsPerPage - rows.length) : 0;
	const isSelected = (id) => selected.findIndex(m => m.id == id) !== -1;
	const numSelected = selected.length;
	const rowCount = rows.length;


	const handleChangePage = (event, newPage) => {
		setPage(newPage);
	};

	const handleSelectAllClick = (event) => {
		if (event.target.checked) {
			const newSelecteds = rows.map((n) => n);
			setSelected(newSelecteds);
			return;
		}
		setSelected([]);
		};

	const handleCheckboxSelect = (event, member) => {
		const selectedIndex = selected.findIndex(m => m.id == member.id);
		let newSelected = [];

		if (selectedIndex === -1) {
			newSelected = newSelected.concat(selected, member);
		} else if (selectedIndex === 0) {
			newSelected = newSelected.concat(selected.slice(1));
		} else if (selectedIndex === selected.length - 1) {
			newSelected = newSelected.concat(selected.slice(0, -1));
		} else if (selectedIndex > 0) {
			newSelected = newSelected.concat(
			selected.slice(0, selectedIndex),
			selected.slice(selectedIndex + 1),
			);
		}

		setSelected(newSelected);
	};
	
	
	const handleOpen = () => setModalOpen(true);
	const handleClose = () => setModalOpen(false);
	
	const handleEdit = (event, member) => {
		setEditRow(member);
		handleOpen(); // open modal to edit data
	};
	
	const handleDelete = (event, member) => {
		const currentRows = rows.slice();
		const memberRowIndex = currentRows.findIndex(r => r.id == member.id);

		console.log("INDEX Of MEMBER",memberRowIndex);
		
		if (memberRowIndex >= 0) {
			currentRows.splice(memberRowIndex, 1);
			console.log("AFTER REMOVING ROW",currentRows);
		}
		setRowsInMemoryAndState(currentRows);
		console.log("AFTER SETTIGN ROW",rows);

	};

	const handleDeleteSelected = (event) => {
		let newRows = [];
		let currentRows = rows.slice();
		
		currentRows.map(member => {
			if (!isSelected(member.id)) {
				newRows.push(member)
			}
		})
		console.log("AFTER REMOVING ROW",newRows);
		setRowsInMemoryAndState(newRows);
	}

	const editMemberData = (event, id, {name, email, role}) => {
        // event.preventDefault();
        console.log("INSIDEEDIT MEMBER")
        const modifiedRow = {
            id: id,
            name: name,
            email: email,
            role: role
        }

        let currentRows = rows.slice();
        let memberIndex = currentRows.findIndex(r => r.id == id);
        currentRows.splice(memberIndex, 1, modifiedRow);

		let updatedRows = currentRows.slice();
        console.log('UPDATED ROWSSS',updatedRows);
        debugger;
        sessionStorage.setItem('memberRows', JSON.stringify(updatedRows));
        
		setRows(updatedRows);
}


	return (
		<Paper sx={{  overflow: 'hidden', margin:"5% 5%" }}>
			<SearchBar setSearchTerm={setSearchTerm} />
			<TableContainer sx={{ maxHeight: 600 }}>
				<Table stickyHeader aria-label="custom pagination table" >
					<TableHead >
						<TableRow key="header_title" >
							<TableCell sx={{background:'#dceaff'}} component="th" scope="row" align="center">
								<Checkbox
									id='selectAllCheckbox'
									color="primary"
									indeterminate={numSelected > 0 && numSelected < rowCount}
									checked={rowCount > 0 && numSelected === rowCount}
									onChange={handleSelectAllClick}
									inputProps={{
									'aria-label': 'select all members',
									}}
								/>
							</TableCell>
							{
								columns.map((col) => (
									<TableCell sx={{background:'#dceaff'}} component="th" scope="row" align="center">
										<b>{col}</b>
									</TableCell>
								))
							}
						</TableRow>
					</TableHead>
					<TableBody>
						{
							(rowsPerPage > 0
								? rows.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
								: rows
							).map((row, index) => {
								const isItemSelected = isSelected(row.id);
								const labelId = `enhanced-table-checkbox-${index}`;
								const highlightSelected = isItemSelected ? true : false;
								return (
									<TableRow key={row.id+row.name} hover selected={highlightSelected}>
										<TableCell padding="checkbox" align="center" >
											<Checkbox
												id='selectCheckbox'
												onClick={(event) => handleCheckboxSelect(event, row)}
												color="primary"
												checked={isItemSelected}
												inputProps={{
													'aria-labelledby': labelId,
												}}
											/>
										</TableCell>
										<TableCell  align="center">
											{row.id}
										</TableCell>
										<TableCell  align="center">
											{row.name}
										</TableCell>
										<TableCell  align="center">
											{row.email}
										</TableCell>
										<TableCell  align="center">
											{row.role}
										</TableCell>
										<TableCell  align="center">
											<IconWrapper>
												<IconButton aria-label="edit" size="large" onClick={(event) => handleEdit(event, row)}>
													<ModeEditOutlineIcon />
												</IconButton>
												<IconButton aria-label="edit" size="large" onClick={(event) => handleDelete(event, row)}>
													<DeleteIcon sx={{color:"red"}} />
												</IconButton>
											</IconWrapper>
										</TableCell>
									</TableRow>
								)
						})
						}

						{emptyRows > 0 && (
							<TableRow style={{ height: 91 * emptyRows }}>
								<TableCell colSpan={6} />
							</TableRow>
						)}
					</TableBody>

					<TableFooter sx={{bottom: 0, zIndex: 2, position: 'sticky', background:'#f5f5f5'}}>
						<TableRow className="tb-footer">
							<TableCell colSpan={1} >
								{ 
									selected.length 
										?
									<IconButton size='50px' onClick={(event) => handleDeleteSelected()}>
										<DeleteIcon />
									</IconButton>  
										:
									''
								}
							</TableCell>
							
							<TableCell colSpan={5} >
								<PaginationWrapper>
									<TablePagination
										rowsPerPageOptions={[]}
										count={rows.length}
										rowsPerPage={rowsPerPage}
										page={page}
										onPageChange={handleChangePage}
										ActionsComponent={TablePaginationActions}
										sx={{width:'100%', ml:100}}
									/>
								</PaginationWrapper>
							</TableCell>
						</TableRow>
					</ TableFooter>
				</Table>
				{
					modalOpen && <EditRowModal openModal={true} member={editRow} rows={rows} setRows={editMemberData} handleClose={handleClose} />
				}
			</TableContainer>
		</Paper>
	);
}
