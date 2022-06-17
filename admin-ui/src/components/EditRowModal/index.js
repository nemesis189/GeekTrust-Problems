import React, { useState, useEffect } from "react";

import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';


const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
};



export default function EditRowModal(props) {
    const { member, setRows, handleClose} = props;
    const [name, setName] = useState(member.name);
    const [email, setEmail] = useState(member.email);
    const [role, setRole] = useState(member.role);
    
    const [open, setOpen] = useState(true);
    

    return (
        <div>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={style} component="form" onSubmit={(event) => setRows(event, member.id, {name, email, role})}>
						<Grid container spacing={3}>
							<Grid item xs={12} sm={12}>
                                <Typography id="modal-modal-title" variant="h6" component="h2">
                                    <b>Edit Member Id - {member.id}</b>
                                </Typography>
							</Grid>
							<Grid item xs={12} sm={12}>
								<TextField
									required
									id="name"
									label="Name"
									name="name"
									value={name}
									onChange={(event) => setName(event.target.value)}
									variant="outlined"
								/>
							</Grid>
							<Grid item xs={12} sm={12}>
								<TextField
									required
									id="email"
									label="Email"
									name="email"
									value={email}
									onChange={(event) => setEmail(event.target.value)}
									variant="outlined"
								/>
							</Grid>
							<Grid item xs={12} sm={12}>
								<TextField
									required
									id="role"
									label="Role"
									name="role"
									value={role}
									onChange={(event) => setRole(event.target.value)}
									variant="outlined"
								/>
							</Grid>
							<Grid item xs={12} sm={12} >
                                <Button variant="contained" type="submit" >
                                    Done
                                </Button>
                                <Button variant="contained" color="error" onClick={(event) => handleClose()} >
                                    Cancel
                                </Button>
							</Grid>
						</Grid>
					</Box>
            </Modal>
        </div>
    );
}
