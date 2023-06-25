"""Type Analyze Pass."""
import jaclang.jac.absyntree as ast
from jaclang.jac.passes.ir_pass import Pass
from jaclang.jac.sym_table import SymbolTable


class TypeAnalyzePass(Pass):
    """Type inference and checking pass."""

    def before_pass(self) -> None:
        """Initialize pass."""
        self.sym_tab = SymbolTable("global")

    def exit_parse(self, node: ast.Parse) -> None:
        """Sub objects.

        name: str,
        """

    def exit_token(self, node: ast.Token) -> None:
        """Sub objects.

        name: str,
        value: str,
        col_start: int,
        col_end: int,
        """

    def exit_name(self, node: ast.Name) -> None:
        """Sub objects.

        name: str,
        value: str,
        col_start: int,
        col_end: int,
        already_declared: bool,
        """

    def exit_constant(self, node: ast.Constant) -> None:
        """Sub objects.

        name: str,
        value: str,
        col_start: int,
        col_end: int,
        typ: type,
        """

    def exit_module(self, node: ast.Module) -> None:
        """Sub objects.

        name: str,
        doc: Token,
        body: Elements,
        mod_path: str,
        """

    def exit_elements(self, node: ast.Elements) -> None:
        """Sub objects.

        elements: list['GlobalVars | Test | ModuleCode | Import | Architype | Ability | AbilitySpec'],
        """

    def exit_global_vars(self, node: ast.GlobalVars) -> None:
        """Sub objects.

        doc: Optional[DocString],
        access: Optional[Token],
        assignments: AssignmentList,
        """

    def exit_test(self, node: ast.Test) -> None:
        """Sub objects.

        name: Token,
        doc: Optional[DocString],
        description: Token,
        body: CodeBlock,
        """

    def exit_module_code(self, node: ast.ModuleCode) -> None:
        """Sub objects.

        doc: Optional[DocString],
        body: CodeBlock,
        """

    def exit_doc_string(self, node: ast.DocString) -> None:
        """Sub objects.

        value: Optional[Token],
        """

    def exit_import(self, node: ast.Import) -> None:
        """Sub objects.

        lang: Token,
        path: ModulePath,
        alias: Optional[Token],
        items: Optional[ModuleItems],
        is_absorb: bool,
        """

    def exit_module_path(self, node: ast.ModulePath) -> None:
        """Sub objects.

        path: list[Token],
        """

    def exit_module_item(self, node: ast.ModuleItem) -> None:
        """Sub objects.

        name: Token,
        alias: Optional[Token],
        """

    def exit_module_items(self, node: ast.ModuleItems) -> None:
        """Sub objects.

        items: list['ModuleItem'],
        """

    def exit_architype(self, node: ast.Architype) -> None:
        """Sub objects.

        name: Token,
        typ: Token,
        doc: Optional[DocString],
        decorators: Optional[Decorators],
        access: Optional[Token],
        base_classes: BaseClasses,
        body: Optional[ArchBlock],
        """

    def exit_arch_def(self, node: ast.ArchDef) -> None:
        """Sub objects.

        doc: Optional[DocString],
        mod: Optional[NameList],
        arch: ObjectRef | NodeRef | EdgeRef | WalkerRef,
        body: ArchBlock,
        """

    def exit_decorators(self, node: ast.Decorators) -> None:
        """Sub objects.

        calls: list['ExprType'],
        """

    def exit_base_classes(self, node: ast.BaseClasses) -> None:
        """Sub objects.

        base_classes: list['NameList'],
        """

    def exit_ability(self, node: ast.Ability) -> None:
        """Sub objects.

        name: Token,
        is_func: bool,
        doc: Optional[DocString],
        decorators: Optional[Decorators],
        access: Optional[Token],
        signature: FuncSignature | TypeSpec | EventSignature,
        body: CodeBlock,
        """

    def exit_ability_def(self, node: ast.AbilityDef) -> None:
        """Sub objects.

        doc: Optional[DocString],
        mod: Optional[NameList],
        ability: AbilityRef,
        body: CodeBlock,
        """

    def exit_ability_spec(self, node: ast.AbilitySpec) -> None:
        """Sub objects.

        doc: Optional[DocString],
        name: Token,
        arch: ObjectRef | NodeRef | EdgeRef | WalkerRef,
        mod: Optional[NameList],
        signature: Optional[FuncSignature],
        body: CodeBlock,
        """

    def exit_arch_block(self, node: ast.ArchBlock) -> None:
        """Sub objects.

        members: list['ArchHas | Ability'],
        """

    def exit_arch_has(self, node: ast.ArchHas) -> None:
        """Sub objects.

        doc: Optional[DocString],
        access: Optional[Token],
        vars: HasVarList,
        """

    def exit_has_var(self, node: ast.HasVar) -> None:
        """Sub objects.

        name: Token,
        type_tag: TypeSpec,
        value: Optional[ExprType],
        """

    def exit_has_var_list(self, node: ast.HasVarList) -> None:
        """Sub objects.

        vars: list['HasVar'],
        """

    def exit_type_spec(self, node: ast.TypeSpec) -> None:
        """Sub objects.

        typ: Token | NameList,
        list_nest: TypeSpec,
        dict_nest: TypeSpec,
        """

    def exit_event_signature(self, node: ast.EventSignature) -> None:
        """Sub objects.

        event: Token,
        arch_tag_info: Optional[NameList | Token],
        """

    def exit_name_list(self, node: ast.NameList) -> None:
        """Sub objects.

        names: list[Token],
        dotted: bool,
        """

    def exit_func_signature(self, node: ast.FuncSignature) -> None:
        """Sub objects.

        params: Optional[FuncParams],
        return_type: Optional[TypeSpec],
        """

    def exit_func_params(self, node: ast.FuncParams) -> None:
        """Sub objects.

        params: list['ParamVar'],
        """

    def exit_param_var(self, node: ast.ParamVar) -> None:
        """Sub objects.

        name: Token,
        unpack: Optional[Token],
        type_tag: TypeSpec,
        value: Optional[ExprType],
        """

    def exit_code_block(self, node: ast.CodeBlock) -> None:
        """Sub objects.

        stmts: list['StmtType'],
        """

    def exit_if_stmt(self, node: ast.IfStmt) -> None:
        """Sub objects.

        condition: ExprType,
        body: CodeBlock,
        elseifs: Optional[ElseIfs],
        else_body: Optional[ElseStmt],
        """

    def exit_else_ifs(self, node: ast.ElseIfs) -> None:
        """Sub objects.

        elseifs: list['IfStmt'],
        """

    def exit_else_stmt(self, node: ast.ElseStmt) -> None:
        """Sub objects.

        body: CodeBlock,
        """

    def exit_try_stmt(self, node: ast.TryStmt) -> None:
        """Sub objects.

        body: CodeBlock,
        excepts: Optional[ExceptList],
        finally_body: Optional[FinallyStmt],
        """

    def exit_except(self, node: ast.Except) -> None:
        """Sub objects.

        typ: ExprType,
        name: Optional[Token],
        body: CodeBlock,
        """

    def exit_except_list(self, node: ast.ExceptList) -> None:
        """Sub objects.

        excepts: list['Except'],
        """

    def exit_finally_stmt(self, node: ast.FinallyStmt) -> None:
        """Sub objects.

        body: CodeBlock,
        """

    def exit_iter_for_stmt(self, node: ast.IterForStmt) -> None:
        """Sub objects.

        iter: Assignment,
        condition: ExprType,
        count_by: ExprType,
        body: CodeBlock,
        """

    def exit_in_for_stmt(self, node: ast.InForStmt) -> None:
        """Sub objects.

        name: Token,
        collection: ExprType,
        body: CodeBlock,
        """

    def exit_dict_for_stmt(self, node: ast.DictForStmt) -> None:
        """Sub objects.

        k_name: Token,
        v_name: Token,
        collection: ExprType,
        body: CodeBlock,
        """

    def exit_while_stmt(self, node: ast.WhileStmt) -> None:
        """Sub objects.

        condition: ExprType,
        body: CodeBlock,
        """

    def exit_raise_stmt(self, node: ast.RaiseStmt) -> None:
        """Sub objects.

        cause: Optional[ExprType],
        """

    def exit_assert_stmt(self, node: ast.AssertStmt) -> None:
        """Sub objects.

        condition: ExprType,
        error_msg: Optional[ExprType],
        """

    def exit_ctrl_stmt(self, node: ast.CtrlStmt) -> None:
        """Sub objects.

        ctrl: Token,
        """

    def exit_delete_stmt(self, node: ast.DeleteStmt) -> None:
        """Sub objects.

        target: ExprType,
        """

    def exit_report_stmt(self, node: ast.ReportStmt) -> None:
        """Sub objects.

        expr: ExprType,
        """

    def exit_return_stmt(self, node: ast.ReturnStmt) -> None:
        """Sub objects.

        expr: Optional[ExprType],
        """

    def exit_yield_stmt(self, node: ast.YieldStmt) -> None:
        """Sub objects.

        expr: Optional[ExprType],
        """

    def exit_ignore_stmt(self, node: ast.IgnoreStmt) -> None:
        """Sub objects.

        target: ExprType,
        """

    def exit_visit_stmt(self, node: ast.VisitStmt) -> None:
        """Sub objects.

        typ: Optional[Token],
        target: Optional[ExprType],
        else_body: Optional[ElseStmt],
        """

    def exit_revisit_stmt(self, node: ast.RevisitStmt) -> None:
        """Sub objects.

        hops: Optional[ExprType],
        else_body: Optional[ElseStmt],
        """

    def exit_disengage_stmt(self, node: ast.DisengageStmt) -> None:
        """Sub objects."""

    def exit_sync_stmt(self, node: ast.SyncStmt) -> None:
        """Sub objects.

        target: ExprType,
        """

    def exit_assignment(self, node: ast.Assignment) -> None:
        """Sub objects.

        is_static: bool,
        target: AtomType,
        value: ExprType,
        """

    def exit_binary_expr(self, node: ast.BinaryExpr) -> None:
        """Sub objects.

        left: ExprType,
        right: ExprType,
        op: Token,
        """

    def exit_if_else_expr(self, node: ast.IfElseExpr) -> None:
        """Sub objects.

        condition: BinaryExpr | IfElseExpr,
        value: ExprType,
        else_value: ExprType,
        """

    def exit_unary_expr(self, node: ast.UnaryExpr) -> None:
        """Sub objects.

        operand: ExprType,
        op: Token,
        """

    def exit_spawn_object_expr(self, node: ast.SpawnObjectExpr) -> None:
        """Sub objects.

        target: ExprType,
        """

    def exit_unpack_expr(self, node: ast.UnpackExpr) -> None:
        """Sub objects.

        target: ExprType,
        is_dict: bool,
        """

    def exit_multi_string(self, node: ast.MultiString) -> None:
        """Sub objects.

        strings: list['Token | FString'],
        """

    def exit_list_val(self, node: ast.ListVal) -> None:
        """Sub objects.

        values: list['ExprType'],
        """

    def exit_expr_list(self, node: ast.ExprList) -> None:
        """Sub objects.

        values: list['ExprType'],
        """

    def exit_dict_val(self, node: ast.DictVal) -> None:
        """Sub objects.

        kv_pairs: list['KVPair'],
        """

    def exit_list_compr(self, node: ast.ListCompr) -> None:
        """Sub objects.

        out_expr: ExprType,
        name: Token,
        collection: ExprType,
        conditional: Optional[ExprType],
        """

    def exit_dict_compr(self, node: ast.DictCompr) -> None:
        """Sub objects.

        outk_expr: ExprType,
        outv_expr: ExprType,
        k_name: Token,
        v_name: Optional[Token],
        collection: ExprType,
        conditional: Optional[ExprType],
        """

    def exit_k_v_pair(self, node: ast.KVPair) -> None:
        """Sub objects.

        key: ExprType,
        value: ExprType,
        """

    def exit_atom_trailer(self, node: ast.AtomTrailer) -> None:
        """Sub objects.

        target: AtomType,
        right: IndexSlice | ArchRefType | Token,
        null_ok: bool,
        """

    def exit_func_call(self, node: ast.FuncCall) -> None:
        """Sub objects.

        target: AtomType,
        params: Optional[ParamList],
        """

    def exit_param_list(self, node: ast.ParamList) -> None:
        """Sub objects.

        p_args: Optional[ExprList],
        p_kwargs: Optional[AssignmentList],
        """

    def exit_assignment_list(self, node: ast.AssignmentList) -> None:
        """Sub objects.

        values: list['ExprType'],
        """

    def exit_index_slice(self, node: ast.IndexSlice) -> None:
        """Sub objects.

        start: ExprType,
        stop: Optional[ExprType],
        """

    def exit_global_ref(self, node: ast.GlobalRef) -> None:
        """Sub objects.

        name: Token,
        """

    def exit_here_ref(self, node: ast.HereRef) -> None:
        """Sub objects.

        name: Optional[Token],
        """

    def exit_visitor_ref(self, node: ast.VisitorRef) -> None:
        """Sub objects.

        name: Optional[Token],
        """

    def exit_node_ref(self, node: ast.NodeRef) -> None:
        """Sub objects.

        name: Token,
        """

    def exit_edge_ref(self, node: ast.EdgeRef) -> None:
        """Sub objects.

        name: Token,
        """

    def exit_walker_ref(self, node: ast.WalkerRef) -> None:
        """Sub objects.

        name: Token,
        """

    def exit_object_ref(self, node: ast.ObjectRef) -> None:
        """Sub objects.

        name: Token,
        """

    def exit_ability_ref(self, node: ast.AbilityRef) -> None:
        """Sub objects.

        name: Token,
        """

    def exit_edge_op_ref(self, node: ast.EdgeOpRef) -> None:
        """Sub objects.

        filter_cond: Optional[ExprType],
        edge_dir: EdgeDir,
        """

    def exit_disconnect_op(self, node: ast.DisconnectOp) -> None:
        """Sub objects.

        filter_cond: Optional[ExprType],
        edge_dir: EdgeDir,
        """

    def exit_connect_op(self, node: ast.ConnectOp) -> None:
        """Sub objects.

        spawn: Optional[ExprType],
        edge_dir: EdgeDir,
        """

    def exit_spawn_ctx(self, node: ast.SpawnCtx) -> None:
        """Sub objects.

        spawns: list[Assignment],
        """

    def exit_filter_ctx(self, node: ast.FilterCtx) -> None:
        """Sub objects.

        compares: list[BinaryExpr],
        """

    def exit_f_string(self, node: ast.FString) -> None:
        """Sub objects.

        parts: list['Token | ExprType'],
        """